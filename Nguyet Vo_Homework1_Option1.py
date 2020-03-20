import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola", "splash of simple syrup"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top", "twist of lemon"]
}

adjectives = ["Fluffy","Stinking","Dangerous","Deadly","Beautiful","Ferocious","Salty","Rusty","Bloody"]
nouns = ["Coffin","Mast","Coffin","Beard","Scabbard","Blunderbus","Dog","Bilge","Grog"]

def askQuestions():
  """Ask a user a series of questions about taste preferences"""
  choices = {}
  for key, value in questions.items():
    answer = input(value)
    if (answer == "y") or (answer == "yes"):
      choices[key] = True
    else:
      choices[key] = False
  return choices
    

def mix(choices):
  """Construct drink based on taste preferences"""
  drink = []
  for key, value in ingredients.items():
    if choices[key]:
      drink.append(random.choice(value))
  return drink
  
if __name__ == '__main__':
  userChoices = askQuestions()
  drink = mix(userChoices)
  drinkname = random.choice(adjectives) + " " + random.choice(nouns)
  print ("")
  print ("Here your drink, The " + drinkname)
  for ingredient in drink:
    print ("a " + ingredient)
