"""
Name: example/pysimplebot
Made By: Mads Hermansen
Github: https://github.com/KarlofKuwait
Date: 15/02/20
Notes: Discord module required
"""

import pysimplebot

bot1 = pysimplebot.Client()
bot1.token = "NTgzNzM1NzIzMzg4MDQzMjY5.Xkg1lg.KWVPHl_tmy7CoW6yQKo_jvxsTWs"
bot1.onready = "print('hello world')"
bot1.game = "game"
bot1.respond = [[["hello", "hi", "lol", "kek"], ["1", "2", "3", "4", "5"]],
                [["!coinflip"], ["heads", "tails"]]]
bot1.joinalert = "'Welcome {0.mention} to {1.name}!'.format(member, server)"
bot1.start()


