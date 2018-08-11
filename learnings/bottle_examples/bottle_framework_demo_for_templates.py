import bottle

# cookies also implemented

@bottle.route("/")
def template_code():
    data_dict = {"Name": "Amandeep",
                 "Interests":["Dreaming", "Gyming", "Swimming"]
                 }
    return bottle.template("profile", data_dict)


@bottle.route("/forminput", method="POST")
def form_input():
    cookie = bottle.request.get_cookie("name")
    get_field = bottle.request.forms.get('name')
    if cookie == None:
        bottle.response.set_cookie("name", get_field)
        return get_field
    else:
        return cookie

bottle.debug(True)
bottle.run(host="localhost", port=8080)