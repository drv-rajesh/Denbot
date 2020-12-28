import discord
import os

from keep import keep
from random import randint

from funcs import fetch_quote
from funcs import fetch_joke
from funcs import fetch_rng
from funcs import fetch_card
from funcs import fetch_colour
from funcs import fetch_tz
from funcs import fetch_weather
from funcs import fetch_det_weather
from funcs import fetch_news

#------------------------------------
client = discord.Client()
#------------------------------------

@client.event
async def on_ready():
  print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('%echo'):
    await message.channel.send('Echoing back.')
  
  if message.content.startswith('%about'):
    await message.channel.send('Denbot is a bot created by Dhruv Rajesh for all purpose use in his server, Dhruv\'s Den.')
  
  if message.content.startswith('%commands'):
    await message.channel.send("""
**Currently Implemented Commands** \n
*General*
`%echo`: Tests Denbot by echoing back.
`%about`: Displays info about Denbot.
`%commands`: Displays Denbot's commands.
`%ghub`: Displays Denbot's GitHub repository.
`%server`: Displays the server Denbot is running on.

*Leisure*
`%quote`: Fetches a random inspirational quote.
`%joke`: Fetches a random dad joke.
`%coin`: Flips a coin.
`%dice`: Rolls a die.
`%rng params:start,stop`: Gets a random number between `start` and `stop`, inclusive.
`%card`: Draws a card from a shuffled deck.
`%colour`: Fetches a random colour.

*Data*
`%time params:timezone`: Displays time for `timezone`.
`%weather params:city`: Displays weather for `city`.
`%weadet params:city`: Displays detailed weather for `city`.
`%news params:country`: Displays top headline for `country`.
    """)

  if message.content.startswith('%time'):
    try:
      tz = message.content.lower().split(" ")[1]
      await message.channel.send(fetch_tz(tz))
    except:
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

keep()
client.run(os.getenv('TOKEN'))
