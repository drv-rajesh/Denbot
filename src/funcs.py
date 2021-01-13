import os
import requests
import json
import pytz
import time
import datetime
import urllib.parse

from random import randint

def fetch_uptime():
  return time.time()

#------

def play_rpg():
  intro = "It's a dark and stormy night. You are in a dark room, and unbeknownst to you, a threat lurks all around the place you are in - in fact it binds all living things in silence. You ponder upon the possibilities of what could have led you here, only to realize that you can't think due to a throbbing sound inside your head. Where do you go (N, S, E, or W)?"

  return intro

#------

def fetch_activity():
  activity = requests.get("https://www.boredapi.com/api/activity").json()

  name = activity['activity']
  cat = activity['type']
  participants = activity['participants']

  return name, cat, participants

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

def fetch_age(name):
  age = requests.get(f"https://api.agify.io?name={name}").json()

  return age['age']

def fetch_sent(sentence):
  headers = {'Accept': 'application/json', "Content-Type": "application/json"}
  params = {"text": sentence}

  analysis = requests.post("https://sentim-api.herokuapp.com/api/v1/", headers=headers, json=params).json()

  return analysis['result']['type'], analysis['result']['polarity']


def fetch_dict(word):
  fetch = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}").json()

  word = fetch[0]['word']
  phonetics = fetch[0]['phonetics'][0]['text']
  part = fetch[0]['meanings'][0]['partOfSpeech']
  definition = fetch[0]['meanings'][0]['definitions'][0]['definition']
  example = fetch[0]['meanings'][0]['definitions'][0]['example']

  return word, phonetics, part, definition, example

def fetch_mathjs(expression):
  fetch = requests.get(f"http://api.mathjs.org/v4/?expr={urllib.parse.quote(expression)}").json()

  return fetch

def fetch_tz(tz):
  now = datetime.datetime.now(pytz.timezone(tz)).strftime("%H:%M:%S")
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

def fetch_loc(city):
  fetch = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.getenv('WEAKEY')}"
  fetch = requests.get(fetch).json()

  lat = round(fetch["coord"]["lat"], 2)
  long = round(fetch["coord"]["lon"], 2)

  return lat, long

def fetch_short(url):
  fetch = requests.post("https://cleanuri.com/api/v1/shorten", data={"url": url}).json()

  return fetch['result_url']
