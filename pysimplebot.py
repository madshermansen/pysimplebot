"""
Name: pysimplebot
Made By: Mads Hermansen
Github: https://github.com/KarlofKuwait
Date: 15/02/20
Notes: Discord module required
"""

import random
import discord
# from discord.ext import commands # user = commands.Bot(command_prefix=".") bot example


class Client:
    def __init__(self):
        self.joinalert = None
        self.game = None
        self.respond = None
        self.onready = None
        self.token = None

    def start(self):
        token = self.token
        client = discord.Client()

        if "onready" in dir(self):
            @client.event
            async def on_ready():
                eval(self.onready)
                if "game" in dir(self):
                    await client.change_presence(status=discord.Status.idle, activity=discord.Game(self.game))

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
                            if len(i) > 1:
                                await channel.send(random.choice(i[1]))

        if "joinalert" in dir(self):
            @client.event
            async def on_member_join(member):
                server = member.server
                if server.system_channel is not None:
                    to_send = eval(self.joinalert)
                    await server.system_channel.send(to_send)

        client.run(token)
