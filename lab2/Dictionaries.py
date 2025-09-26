#ORDERED, CHANGEABLE, DO NOT ALLOW DUPLICATES
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

x = thisdict.get("model")
x = thisdict.keys()
X = thisdict.values()
x = thisdict.items()

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})

#REMOVING
dict.clear()
del thisdict["model"]
del dict
thisdict.popitem()
