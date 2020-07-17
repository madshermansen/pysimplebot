import pysimplebot
import random

Guessingbot = pysimplebot.Client()
Guessingbot.token = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
Guessingbot.onready = "print('I am ready')"
Guessingbot.respond = [[["hi"],["Hello"]]]
Guessingbot.cc1 = """@client.event
async def on_message(message):
    if message.content.startswith("Guess") or message.content.startswith("That"):
        return
    channel = message.channel
    guess = random.randint(1,20)
    if message.content == str(guess1):
        await channel.send("That is the right number! Number has been reset")
    else:
        await channel.send("That is incorrect, Number has been reset")     
    await channel.send("Guess a number between 1-20")
    return
"""
Guessingbot.start()