import pysimplebot

bot1 = pysimplebot.Client()
bot1.token = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
bot1.game = "game"
bot1.respond = [[["hello", "hi", "lol", "kek"], ["1", "2", "3", "4", "5"]],
                [["!coinflip"], ["heads", "tails"]]]
bot1.start()
