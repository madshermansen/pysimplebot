"""
Name: pysimplebot
Made By: Mads Hermansen
Github: https://github.com/KarlofKuwait
Date: 15/02/20
Notes: Discord module required
"""

import random
import discord
from discord.ext import commands


class Client:
    def __init__(self):
        pass

    # Function to call when starting bot
    def start(self):
        token = self.token
        client = discord.Client()

        # Runs when bot is ready (self.onready)
        @client.event
        async def on_ready():
            if "onready" in dir(self):
                eval(self.onready)
            if "game" in dir(self):
                await client.change_presence(status=discord.Status.idle, activity=discord.Game(self.game))

        # Respond to messages from user (self.respond)
        if "respond" in dir(self):
            @client.event
            async def on_message(message):
                botmessage = self.respond
                channel = message.channel
                if message.author == client.user:
                    return
                for i in botmessage:
                    for j in range(len(i[0])):
                        if message.content.startswith(i[0][j]):
                            if len(i) == 1:
                                await channel.send(i[1])
                                return
                            if len(i) > 1:
                                await channel.send(random.choice(i[1]))
                                return

        # Join alerts for new members joining server (self.joinalert)
        if "joinalert" in dir(self):
            @client.event
            async def on_member_join(member):
                server = member.server
                if server.system_channel is not None:
                    to_send = eval(self.joinalert)
                    await server.system_channel.send(to_send)

        # User running custom code (self.cc1-1000)
        cc = []
        for i in range(1000):
            if "cc" + str(i) in dir(self):
                cc.append("cc" + str(i))
        for customcode in cc:
            code = "self." + customcode
            exec(eval(code))


        client.run(token)

class Bot:
    def __init__(self):
        pass

    def start(self):
        token = self.token
        if "description" in dir(self) and "prefix" in dir(self):
            bot = commands.Bot(command_prefix=self.prefix, description=self.description)
        elif "prefix" in dir(self):
            bot = commands.Bot(command_prefix=self.prefix, description="")
        else:
            bot = commands.Bot(command_prefix="", description="")

        @bot.event
        async def on_ready():
            if "onready" in dir(self):
                eval(self.onready)

        # User running custom code (self.cc1-1000)
        cc = []
        for i in range(1000):
            if "cc" + str(i) in dir(self):
                cc.append("cc" + str(i))
        for customcode in cc:
            code = "self." + customcode
            exec(eval(code))


        bot.run(token)
