import discord
import random

class bot:
    def start(self):
        #
        token = self.token
        client = discord.Client()
        #

        @client.event
        async def on_ready():
            try:
                eval(self.onready)
            except:
                pass
            try:
                await client.change_presence(status=discord.Status.idle, activity=discord.Game(self.game))
            except:
                pass


        @client.event
        async def on_message(message):
            botmessage = self.respond
            channel = message.channel
            if message.author == client.user:
                return
            for i in botmessage:
                for j in range(len(i)):
                    if message.content.startswith(i[0][j]):
                        if len(i) == 1:
                            await channel.send(i[1])
                        if len(i) > 1:
                            await channel.send(random.choice(i[1]))
                        return

        client.run(token)
