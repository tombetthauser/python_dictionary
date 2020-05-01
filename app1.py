from json import load
from difflib import get_close_matches as close
from random import random

data = load(open("data.json"))
words = list(data.keys())

store = {
    "almost": "That's almost a word... Did you mean %s instead? ",
    "sorry ": "That's not even close to a word... Sorry.",
    "here": "Ok, here's the definition for %s.",
    "enter": "Please enter a word: ",
    "alright": "Well alrighty then.",
    "yestup": ('yes', 'y', 'ok')
}

def lookup(word):
  if word in data: return data[word]
  
  word = word.lower()
  if word in data: return data[word]

  matches = close(word, data.keys())
  matchLen = len(matches)

  if matchLen > 0:
    rand = int(random() * matchLen)
    maybe = matches[rand]
    text = store["almost"] % maybe
    resp = input(text)

    if resp.lower() in store["yestup"]: return [store["here"] % maybe] + data[maybe]
    else: return [store["alright"]]
  else: return [store["sorry"]]

word = input(store["enter"])
trans = lookup(word)

for entry in trans: print(entry)
