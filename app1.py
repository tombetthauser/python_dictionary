import json

data = json.load(open("data.json"))
words = list(data.keys())

def translate(word):
  if word in data:
    return data[word]
  else:
    return ["That word is not in this dictionary. Please double-check you're spelling and try again."]

word = input("Enter a word:")
translation = translate(word)

for entry in translation:
  print(entry)