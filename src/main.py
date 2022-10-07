import random

# list of meals based on mood
happy_mood = ["meal 1", "meal 2", "meal 3"]


# chooses random meal from the mood list
def happy_meal():
    meal = happy_mood[random.randint(0, len(happy_mood) - 1)]
    print(meal)


happy_meal()
