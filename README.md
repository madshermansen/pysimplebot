# simplediscordbot
makes it easy to make discord bots using classes

>## Requirements
```
discord.py
```
>## Examples
```python
import pysimplebot

bot1 = pysimplebot.Client()
bot1.token = "token"
bot1.onready = "print('Logged in as ' + client.user.name)"
bot1.game = "!help for help"
bot1.respond = [[["!help", "!Help"], ["What do you need help with?", "Whats up?", "How can I help?"]]]
bot1.joinalert = "'Welcome {0.mention} to {1.name}!'.format(member, server)"
bot1.start()

```
