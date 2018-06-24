# Define a function that sends a message to the bot: send_message
from ai.ml.nlp.chatbots.practise.asis._1_02_EchoBot1 import user_template
from ai.ml.nlp.chatbots.practise.asis._1_02_EchoBot1 import bot_template
from ai.ml.nlp.chatbots.practise.asis._1_02_EchoBot1 import respond


def send_message(message):
    # Print user_template including the user_message
    print(user_template.format(message))
    # Get the bot's response to the message
    response = respond(message)
    # Print the bot template including the bot's response.
    print(bot_template.format(response))

# Send a message to the bot
send_message("hello")