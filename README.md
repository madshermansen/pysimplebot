# simplediscordbot

# Installation

requirements

```
discord.py
```

**Python 3.5.3 or higher is required**

>To install the library without full voice support, you can just run the following command:

```
# Linux/macOS
python3 -m pip install -U discord.py

# Windows
py -3 -m pip install -U discord.py
```

>Otherwise to get voice support you should run the following command:

```
# Linux/macOS
python3 -m pip install -U discord.py[voice]

# Windows
py -3 -m pip install -U discord.py[voice]
```

>To install the development version, do the following:

```
$ git clone https://github.com/Rapptz/discord.py
$ cd discord.py
$ python3 -m pip install -U .[voice]
```

- Taken from https://github.com/Rapptz/discord.py/README.rst

# Examples
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
# Client
```python
bot1 = pysimplebot.Client()
```
**token**

Discord bots token found [here](https://discordapp.com/developers/applications), you will need to create your own

**onready**

The command that will run when the bot has initialized
```python
bot.onready = "print('Successfully logged in)"
```

```python
bot.start()
>>> Successfully logged in
```


**game**

Determines the current game the bot is "playing"


![gameplayed](https://github.com/KarlofKuwait/pysimplebot/blob/master/pysimplebot%20demonstration%20images/Game%20being%20played.png?raw=true)

**respond**

Respond to messages if it startswith *userinput*

*examples*
```python
[
  [["userinput1", "userinput2"], ["response"]],
  [["userinput3", "userinput4", "userinput5"], ["response2", "response3"]], # Bot will choose either response 2 or 3
  ["userinput5", "response4"]
]
```

```python
userinput1
>>> response
userimput3
>>> reponse2
userimput3
>>> reponse3
userinput5
>>> response4
```

**joinalert**

Join alert for new members

**start()**

Function from pysimplebot to begin the bot
