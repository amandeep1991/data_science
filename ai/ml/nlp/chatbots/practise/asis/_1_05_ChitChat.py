# Define variables
from ai.ml.nlp.chatbots.practise.asis._1_02_EchoBot1 import user_template, bot_template

name = "Greg"
weather = "cloudy"

# Define a dictionary with the predefined responses
responses = {
  "what's your name?": "My name is {0}".format(name),
  "what's today's weather?": "The weather is {0}".format(weather),
  "default": "Sorry! what was that?"
}

# Return the matching response if there is one, default otherwise
def respond(message):
    # Check if the message is in the responses
    if message in responses:
        # Return the matching message
        bot_message = responses[message]
    else:
        # Return the "default" message
        bot_message = responses["default"]
    return bot_message


if __name__ == "__main__":
    message = input()
    print(user_template.format(message))
    print(bot_template.format(respond(message)))