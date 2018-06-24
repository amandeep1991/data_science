bot_template = "BOT : {0}"
user_template = "USER : {0}"


# Define a function that responds to a page's message: respond
def respond(message):
    # Concatenate the page's message to the end of a standard bot respone
    bot_message = "I can hear you! You said: '" + message + "'"
    # Return the result
    return bot_message


if __name__ == "__main__":
    message = input()
    print(user_template.format(message))
    print(bot_template.format(respond(message)))