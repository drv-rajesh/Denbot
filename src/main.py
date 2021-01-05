import discord
import os
import time
import datetime
import urllib.parse
import sys

from keep import keep
from random import randint
from replit import db

from funcs import *

#------------------------------------
client = discord.Client()
uptime = fetch_uptime()
#------------------------------------

@client.event
async def on_ready():
  print('Logged in as {0.user}'.format(client))
  await client.change_presence(activity=discord.Game(name='denbot.gg'))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if "hi denbot" in message.content.lower():
    await message.add_reaction("👋")

  if message.content.startswith('%echo'):
    await message.channel.send('Echoing back.')
  
  if message.content.startswith('%about'):
    await message.channel.send('Denbot is a bot created by Dhruv Rajesh for all purpose use in his server, Dhruv\'s Den.')
  
  if message.content.startswith('%commands'):
    await message.author.send("""
**31 Currently Implemented Commands** (Emoji Key: https://tinyurl.com/yb8gxoct) \n
*General (6)*
`%echo`: Tests Denbot by echoing back.
`%about`: Displays info about Denbot.
`%commands`: Displays Denbot's commands.
`%uptime params:🌓format`: Displays Denbot's uptime.
    Example: %uptime hhmmss or %uptime
`%ghub`: Displays Denbot's GitHub repository. ❗
`%server`: Displays the server Denbot is running on. ❗

*Leisure (11)*
`%bored`: Finds an activity for you to do.
`%quote`: Fetches a random inspirational quote.
`%joke`: Fetches a random dad joke.
`%coin`: Flips a coin.
`%dice`: Rolls a die.
`%rng params:start,stop`: Gets a random number between `start` and `stop`, inclusive.
    Example: %rng 1 10 or %rng 13323 2893282
`%card`: Draws a card from a shuffled deck.
`%colour`: Fetches a random colour.
`%age params:name`: Predicts age based on name.
    Example: %age Dhruv
`%me`: Adds yourself to Denbot's database.
`%sent params:sentence`: Perform sentiment analysis on a sentence.
    Example: %sent good is bad or not""")

    await message.author.send("""

*Data (5)*
`%time params:timezone`: Displays time for `timezone`.
    Example: %time Canada/Eastern or %time Canada/Mountain
`%weather params:city`: Displays weather for `city`.
    Example: %weather Toronto or %weather Chandler
`%weadet params:city`: Displays detailed weather for `city`.
    Example: %weadet Toronto or %weadet Chandler
`%news params:country`: Displays top headline for `country`.
    Example: %news CA or %news US
`%loc params:city`: Displays lat and long for `city`.
    Example: %loc Toronto or %loc Chandler
*Server (3)*
`%count`: Returns member count.
`%ls`: Lists all members.
`%cls`: Lists all channels.

*Tools and Utilities (6)*
`%dict params:word`: Get the dictionary data on a word.
    Example: %dict hello or %dict why
`%short params:url`: Shortens a URL.
    Example: %short https://google.ca
`%eval params:expression`: Solve an expression. 🔨
    Example: %eval 2+3
`%encode params:string`: Encodes `string` in URL UTF-8 format.
    Example: %encode 25sjf
`%sizeof params:var`: Shows an object's memory consumption.
    Example: %sizeof 5 or %sizeof efjisf
`%bin params:string`: Converts an object to binary.
    Example: %bin hello or %bin 510
    """)

    await message.channel.send(f"👋 {message.author.mention}! Check your DMs for a list of commands.")

  if message.content.startswith('%uptime'):
    try:
      form = message.content.lower().split(" ")[1]
    except:
      form = "verbose"
    
    current = round(time.time() - uptime)
    verbose = str(datetime.timedelta(seconds=current)).split(":")
    current_non = str(datetime.timedelta(seconds=current))

    if form == "verbose":
      await message.channel.send(f"{int(verbose[0])} hours, {int(verbose[1])} minutes, {int(verbose[2])} seconds")
    elif form == "hhmmss":
      await message.channel.send(current_non)

  if message.content.startswith('%time'):
    try:
      tz = message.content.lower().split(" ")[1]
      await message.channel.send(fetch_tz(tz))
    except IndexError:
      await message.channel.send('Please provide a valid `timezone` parameter.')
  
  if message.content.startswith('%weather'):
    try:
      loc = message.content.lower().split(" ")[1]
      await message.channel.send(f"Temperature: {round(fetch_weather(loc)[0], 2)}°C (Feels like {round(fetch_weather(loc)[1], 2)}°C) \nWeather: {fetch_weather(loc)[2].title()} \nHumidity: {fetch_weather(loc)[3]}")
    except:
      await message.channel.send('Please provide a valid `city` parameter.')
  
  if message.content.startswith('%weadet'):
    try:
      loc = message.content.lower().split(" ")[1]
      await message.channel.send(f"Visibility: {fetch_det_weather(loc)[0]} \nWind: {fetch_det_weather(loc)[1]}")
    except:
      await message.channel.send('Please provide a valid `city` parameter.')
  
  if message.content.startswith('%news'):
    loc = message.content.lower().split(" ")[1]

    await message.channel.send(f"**{fetch_news(loc)[1][0]} by *{fetch_news(loc)[0][0]}*** \n{fetch_news(loc)[2][0]} \n--- \nView full coverage here: {fetch_news(loc)[3][0]}")
  
  if message.content.startswith('%loc'):
    loc = message.content.lower().split(" ")[1]

    latitude = fetch_loc(loc)[0]
    longitude = fetch_loc(loc)[1]

    if latitude > 0: direction = "°N"
    else: direction = "°S"
    if longitude > 0: direction_l = "°E" 
    else: direction_l = "°W"

    await message.channel.send(f"Latitude: {abs(latitude)}{direction} \nLongitude: {abs(longitude)}{direction_l}")
  
  if message.content.startswith('%bored'):
    activity = fetch_activity()

    await message.channel.send(f"""
Here's a {activity[1]} activity:
  `{activity[0]}`
It requires {activity[2]} participant(s).
    """)

  if message.content.startswith('%quote'):
    await message.channel.send(fetch_quote())

  if message.content.startswith('%joke'):
    await message.channel.send(fetch_joke())

  if message.content.startswith('%card'):
    card = fetch_card()

    await message.channel.send(f"{card[0].title()} of {card[1].title()}")

  if message.content.startswith('%colour'):
    col = fetch_colour()

    await message.channel.send(f"`{col[1]}` ({col[0]})")
  
  if message.content.startswith('%age'):
    age = fetch_age(message.content.split(" ")[1])

    await message.channel.send(age)
  
  if message.content.startswith('%sent'):
    sentence = fetch_sent(message.content.split(" ", 1)[1])

    result = sentence[0]
    polarity = sentence[1]

    if str(polarity) == "0.0":
      polarity = 1.0

    await message.channel.send(f"{abs(polarity*100)}% {result}")
  
  if message.content.startswith('%dict'):
    word = message.content.lower().split(" ")[1]
    fetch = fetch_dict(word)

    await message.channel.send(f"""
\"{fetch[0]}\" (Pronounced: \"{fetch[1]}\")
*{fetch[2]}*
**{fetch[3]}**
*{fetch[4]}*
    """)

  if message.content.startswith('%eval'):
    expr = message.content.lower().split(" ")[1]
    
    await message.channel.send(fetch_mathjs(expr))
  
  if message.content.startswith('%coin'):
    if randint(0, 1) == 0:
      await message.channel.send("Heads")
    else:
      await message.channel.send("Tails")
  
  if message.content.startswith('%rng'):
    start = message.content.lower().split(" ")[1]
    stop = message.content.lower().split(" ")[2]
    await message.channel.send(fetch_rng(start, stop))

  if message.content.startswith('%dice'):
    roll = randint(1, 6)
    await message.channel.send(roll)

  if message.content.startswith('%ghub'):
    await message.channel.send("https://github.com/drv-rajesh/Denbot")

  if message.content.startswith('%server'):
    await message.channel.send("https://Denbot.drvrajesh.repl.co")

  if message.content.startswith('%encode'):
    await message.channel.send(urllib.parse.quote(message.content.lower().split(" ")[1]))

  if message.content.startswith('%sizeof'):
    await message.channel.send(str(sys.getsizeof(message.content.lower().split(" ")[1])) + " bytes")
  
  if message.content.startswith("%bin"):
    converted = ''.join(format(i, 'b') for i in bytearray(message.content.lower().split(" ")[1], encoding ='utf-8')) 
    await message.channel.send(converted)
  
  if message.content.startswith("%me"):
    db["User"] = str(message.author)
    await message.channel.send(f"{message.author.mention}, you have been remembered forever.")

  #--------------------------------------

  if message.content.startswith("%count"):
    await message.channel.send(message.guild.member_count)
  
  if message.content.startswith("%ls"):
    for guild in client.guilds:
      for member in guild.members:
        await message.channel.send(member)
  
  if message.content.startswith("%cls"):
    for guild in client.guilds:
      for channel in guild.channels:
        await message.channel.send(channel)
  
  #---------------------------------------

  if message.content.startswith("%short"):
    url = message.content.lower().split(" ")[1]
    await message.channel.send(fetch_short(url))

keep()
client.run(os.getenv('TOKEN'))
