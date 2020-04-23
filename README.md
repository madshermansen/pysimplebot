# simplediscordbot
makes it easy to make discord bots using classes

># Requirements
```
discord.py
```
># Examples
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
> # Client
```python
bot1 = pysimplebot.Client()
```
> **token**

Discord bots token found [here](https://discordapp.com/developers/applications), you will need to create your own

> **onready**

The command that will run when the bot has initialized

> **game**

Determines the current game the bot is "playing"

> **respond**

Respond to messages if it startswith *userinput*

*examples*
```python
[
  [["userinput", "userinput2"], ["response"]],
  [["userinput3", "userinput4", "userinput5"], ["response2", "response3"]], # Bot will choose either response 2 or 3
  ["userinput5", "response4"]
]
```


```python
userinput
>>> response
userimput3
>>> reponse2
userimput3
>>> reponse3
userinput5
>>> response4
```

> **joinalert**

Join alert for new members

> **start()**

Function from pysimplebot to begin the bot
