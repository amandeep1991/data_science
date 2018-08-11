import bottle
from sklearn.linear_model import LogisticRegression

x_train = ""
y_train = ""
x_test  = ""

@bottle.route("/")
def return_prediction_value():
    # all parameters not specified are set to their defaults
    logisticRegr = LogisticRegression()
    logisticRegr.fit(x_train, y_train)
    return logisticRegr.predict(x_test)


bottle.run(host="localhost", port=8080)