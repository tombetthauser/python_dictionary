from json import load
from difflib import get_close_matches as close
from random import random

data = load(open("data.json"))
words = list(data.keys())
word = ""

store = {
    "almost": "That's almost a word... Did you mean %s instead? ",
    "sorry": "That's not even close to a word... Sorry.",
    "thanks": "Thank you for using Tom's python dictionary!\nHope to see you again soon :)\n",
    "here": "Ok, here's the definition / definitions for %s.",
    "yestup": ('y', 'ok', 'yes', 'yup', 'sure'),
    "enter": "\nPlease enter a word: ",
    "alright": "Well alrighty then.",
    "quitup": ('q', 'quit', 'exit'),

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

while True:
  word = input(store["enter"])

  if word in store["quitup"]: 
    print(store["thanks"])
    break
  else: 
    trans = lookup(word)
    for entry in trans: print(entry)
