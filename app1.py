import json

data = json.load(open("data.json"))
words = list(data.keys())

def translate(word):
  return data[word]

word = input("Enter a word:")
translation = translate(word)

for entry in translation:
  print(entry)