import os
import requests
import json
import pytz

from datetime import datetime
from random import randint

def fetch_quote():
  response = requests.get("https://zenquotes.io/api/random")
  quote = json.loads(response.text)[0]['q'] + " -" + json.loads(response.text)[0]['a']
  return quote

def fetch_joke():
  headers = {'Accept': 'application/json'}
  joke = requests.get('https://icanhazdadjoke.com', headers=headers).json().get('joke')
  return joke

def fetch_rng(start, stop):
  num = randint(int(start), int(stop))
  return num

def fetch_card():
  card = requests.get('https://deckofcardsapi.com/api/deck/new/draw/?count=1').json()

  value = card['cards'][0]['value']
  suit = card['cards'][0]['suit']

  return value, suit

def fetch_colour():
  colour = requests.get('http://www.colr.org/json/color/random').json()

  hexa = colour['colors'][0]['hex'].upper()
  name = colour['colors'][0]['tags'][0]['name'].upper()

  return hexa, name 

def fetch_tz(tz):
  now = datetime.now(pytz.timezone(tz)).strftime("%H:%M:%S")
  return now

def fetch_weather(city):
  fetch = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.getenv('WEAKEY')}"
  fetch = requests.get(fetch).json()

  temperature = ((fetch['main']['temp']) - 273.15)
  feels_like = ((fetch['main']['feels_like']) - 273.15)
  weather = fetch['weather'][0]['description']
  humidity = fetch['main']['humidity']

  return temperature, feels_like, weather, humidity

def fetch_det_weather(city):
  fetch = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.getenv('WEAKEY')}"
  fetch = requests.get(fetch).json()

  visibility = (fetch['visibility'])
  wind_speed = (fetch['wind']['speed'])

  return visibility, wind_speed

def fetch_news(country):
  fetch = requests.get(f"https://newsapi.org/v2/top-headlines?country={country}&pageSize=1&apiKey={os.getenv('NEWSKEY')}").json()
  
  authors = []
  titles = []
  descs = []
  urls = []

  authors.append(fetch['articles'][0]['author'])
  titles.append(fetch['articles'][0]['title'])
  descs.append(fetch['articles'][0]['description'])
  urls.append(fetch['articles'][0]['url'])
    
  return authors, titles, descs, urls
