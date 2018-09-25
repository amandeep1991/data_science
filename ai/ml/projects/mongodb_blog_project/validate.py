import pymongo
import urllib2
import urllib
import cookielib
import random
import re
import string
import sys
import getopt

# init the global cookie jar
cj = cookielib.CookieJar()
# declare the variables to connect to db
connection = None
db = None
webhost = "localhost:8082"
mongostr = "mongodb://localhost:27017"
db_name = "blog"

# this script will check that homework 3.2 is correct

# makes a little salt
def make_salt(n):
    salt = ""
    for i in range(n):
        salt = salt + random.choice(string.ascii_letters)
    return salt


# this is a validation script to make sure the blog works correctly.

def create_user(username, password):
    
    global cj

    try:
        print "Trying to create a test user ", username
        url = "http://{0}/signup".format(webhost)

        data = urllib.urlencode([("email",""),("username",username), ("password",password), ("verify",password)])
        request = urllib2.Request(url=url, data=data)
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        f = opener.open(request)

        users = db.users
        # check that the user is in users collection
        user = users.find_one({\'_id\':username})
        if (user == None):
            print "Could not find the test user ", username, "in the users collection."
            return False
        print "Found the test user ", username, " in the users collection"

        # check that the user has been built
        result = f.read()
        expr = re.compile("Welcome\\s+"+ username)
        if expr.search(result):
            return True
        
        print "When we tried to create a user, here is the output we got\
"
        print result
        
        return False
    except:
        print "the request to ", url, " failed, so your blog may not be running."
        raise
        return False


def try_to_login(username, password):

    try:
        print "Trying to login for test user ", username
        url = "http://{0}/login".format(webhost)

        data = urllib.urlencode([("username",username), ("password",password)])
        request = urllib2.Request(url=url, data=data)
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        f = opener.open(request)

        # check for successful login
        result = f.read()
        expr = re.compile("Welcome\\s+"+ username)
        if expr.search(result):
            return True

        print "When we tried to login, here is the output we got\
"
        print result
        return False
    except:
        print "the request to ", url, " failed, so your blog may not be running."
        return False


def add_blog_post(title,post,tags):

    try:
        print "Trying to submit a post with title ", title
        data = urllib.urlencode([("body",post), ("subject",title), ("tags",tags)])
        url = "http://{0}/newpost".format(webhost)
        request = urllib2.Request(url=url, data=data)
        cj.add_cookie_header(request)
        opener = urllib2.build_opener()
        f = opener.open(request)

        # check for successful login
        result = f.read()
        expr = re.compile(title + ".+" + post, re.DOTALL)

        if expr.search(result):
            return True

        print "When we tried to post, here is the output we got\
"
        print result
        return False

    except:
        print "the request to ", url, " failed, so your blog may not be running."
        raise

        return False

def add_blog_comment(title,post):

    try:
        print "+Trying to submit a blog comment for post with title", title
        url = "http://{0}/newcomment".format(webhost)
        
        doc = {}
        check_mongo_for_post(title, post, doc)

        permalink = doc[\'doc\'][\'permalink\']

        comment_name = make_salt(12)
        comment_body = make_salt(12)

        data = urllib.urlencode([("commentName",comment_name), ("commentBody",comment_body), ("permalink",permalink)])
        request = urllib2.Request(url=url, data=data)
        cj.add_cookie_header(request)
        opener = urllib2.build_opener()
        f = opener.open(request)

        # check for successful addition of comment on page
        result = f.read()
        expr = re.compile(title + ".+" + post, re.DOTALL)

        if not expr.search(result):
            print "When we tried to find the comment we posted at the  ", url, " here is what we got"
            print result
            return False


        # check for successful addition of comment..retrieve the doc again
        if(not check_mongo_for_post(title, post, doc)):
            print "Could not find comment in database"
            return False
        
        found = False
        if (\'comments\' in doc[\'doc\']):
            for comment in doc[\'doc\'][\'comments\']:
                if (comment[\'body\'] == comment_body and comment[\'author\'] == comment_name):
                    found = True

        return found

    except:
        print "the request to ", url, " failed, so your blog may not be running."
        raise

        return False


# fetch the blog home page and return the link of the first post
def fetch_blog_home_page(posts):

    try:
        url = "http://{0}/".format(webhost)
        print "Trying to grab the blog home page at url and find the first post.", url
        request = urllib2.Request(url=url)
        cj.add_cookie_header(request)
        opener = urllib2.build_opener()
        f = opener.open(request)

        # Look for a post
        result = f.read()
        expr = re.compile("<a href=\\"([^\\"]+)\\"\\w*?>", re.DOTALL)


        match = expr.search(result)

        if match is not None:
            print "Found a post url: ", match.group(1)
            posts.append(match.group(1))
            return True

        
        print "Hmm, can\'t seem to find a post. Is the blog populated with posts?"
        print "When we tried to read the blog index at ", url, " here is what we got"
        print result
        return False

    except:
        print "the request to ", url, " failed, so your blog may not be running."
        raise

        return False

# gets the likes value off the first commment or returns None
def fetch_likes(url):

    try:
        url = "http://{0}{1}".format(webhost, url)
        print "Trying to grab the number of likes for url ", url
        request = urllib2.Request(url=url)
        cj.add_cookie_header(request)
        opener = urllib2.build_opener()
        f = opener.open(request)


        # let\'s get the first form element
        result = f.read()
        expr = re.compile("<form[^>]*>.*?Likes:\\s*(\\d+)\\s*<.*?</form>", re.DOTALL)

        match = expr.search(result)

        if match is not None:
            print "Likes value ", match.group(1)
            return int(match.group(1))

        print "Can\'t fetch the like value for the first comment. Perhaps the blog entry has no comments?"
        print "When we tried to read the blog permalink at ", url, " here is what we got"
        return None

    except:
        print "the request to ", url, " failed, so your blog may not be running."
        raise

        return None


# gets the likes value off the first commment or returns None
def click_on_like(permalink):

    print "Clicking on Like link for post: ", permalink
    try:
        expr =  re.compile("[^/]+/([^/]+)")
        match = expr.search(permalink)
        if match is None:
            return False

        permalink = match.group(1)
        url = "http://{0}/like".format(webhost)
        # print "Like POST url", url

        data = urllib.urlencode([("permalink",permalink), ("comment_ordinal","0")])
        request = urllib2.Request(url=url, data=data)
        cj.add_cookie_header(request)
        opener = urllib2.build_opener()
        f = opener.open(request)

        return True

    except:
        print "the request to ", url, " failed, so your blog may not be running."
        raise




# command line arg parsing to make folks happy who want to run at mongolabs or mongohq
# this functions uses global vars to communicate. forgive me.
def arg_parsing(argv):

    global webhost
    global mongostr
    global db_name

    try:
        opts, args = getopt.getopt(argv, "-p:-m:-d:")
    except getopt.GetoptError:
        print "usage validate.py -p webhost -m mongoConnectString -d databaseName"
        print "\\twebhost defaults to {0}".format(webhost)
        print "\\tmongoConnectionString default to {0}".format(mongostr)
        print "\\tdatabaseName defaults to {0}".format(db_name)
        sys.exit(2)
    for opt, arg in opts:
        if (opt == \'-h\'):
            print "usage validate.py -p webhost -m mongoConnectString -d databaseName"
            sys.exit(2)
        elif opt in ("-p"):
            webhost = arg
            print "Overriding HTTP host to be ", webhost
        elif opt in ("-m"):
            mongostr = arg
            print "Overriding MongoDB connection string to be ", mongostr
        elif opt in ("-d"):
            db_name = arg
            print "Overriding MongoDB database to be ", db_name
            


# main section of the code
def main(argv):
            
    arg_parsing(argv)
    global connection
    global db

    print "Welcome to the M101 Final Exam, Question 4 Validation Checker"

    # connect to the db (mongostr was set in arg_parsing)
    connection = pymongo.MongoClient(mongostr)
    db = connection[db_name]


    # grab the blog home page and find the first post
    posts = []
    if (not fetch_blog_home_page(posts)):
        print "I can\'t grab the home page of the blog"
        sys.exit(1)

    # now go to the permalink page for that post
    likes_value = fetch_likes(posts[0])

    if (likes_value is  None):
        print "Can\'t fetch the like value"
        sys.exit(1)

    click_on_like(posts[0])

    new_likes_value = fetch_likes(posts[0])

    if (new_likes_value != (likes_value + 1)):
        print "I was not able to increment the likes on a comment"
        print "old likes value was ", likes_value
        print "likes value after I clicked was ", new_likes_value
        print "Sorry, you have not solved it yet."
        sys.exit(1)


    print "Tests Passed for Final 4. Your validation code is 3f837hhg673ghd93hgf8"


if __name__ == "__main__":
    main(sys.argv[1:])
