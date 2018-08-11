import bottle

@bottle.route("/")
def home_page():
    return "Hello World"


@bottle.route("/testpage")
def test_page():
    return "This is test page - Hadipa"

bottle.debug(True) # reload the page for any change, which when I tested didn't work
bottle.run(host="localhost", port=8080)