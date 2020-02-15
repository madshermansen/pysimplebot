import simplediscordbot as sdb

bot1 = sdb.bot()
bot1.token = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
bot1.onready = "print('hello world')"
bot1.game = "game"
bot1.respond = [[["Userinput1", "Userinput1(area2)"], ["Botresponse 0 or 1", "Botresponse 0 or 1"]], ["Userinput2", "Botresponse2"]]
bot1.start()