import random

# list of meals based on mood
# happy_mood = ["meal 1", "meal 2", "meal 3"]
happy_mood = {"meal 1": "recipe 1",
              "meal 2": "recipe 2",
              "meal 3": "recipe 3"}


# chooses random meal from the mood list
def happy_meal():
    # meal = happy_mood[random.randint(0, len(happy_mood) - 1)]
    meal, recipe = random.choice(list(happy_mood.items()))
    print(meal)
    print(recipe)


happy_meal()
