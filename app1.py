from json import load
from difflib import get_close_matches
from random import random

data = load(open("data.json"))
words = list(data.keys())

yesTup = ('yes', 'y', 'ok')
noTup = ('no', 'n', 'nope')

def translate(word):
  word = word.lower()

  if word in data:
    return data[word]

  matches = get_close_matches(word, data.keys())
  matchLen = len(matches)
  if matchLen > 0:
    randomIdx = int(random() * matchLen)
    suggestion = matches[randomIdx]
    text = "That's almost a word... Did you mean %s instead? " % suggestion
    yn = input(text)
    if yn.lower() in yesTup:
      return ["Ok, here's the definition for %s." % suggestion] + data[suggestion]
  else:
    return ["That word is not in this dictionary. Please double-check you're spelling and try again."]

word = input("Please enter a word: ")
translation = translate(word)

for entry in translation:
  print(entry)
