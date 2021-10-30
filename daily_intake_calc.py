"""This can be a function that does the calculation or searches the web."""

import random


def get_daily_intake(weight, height, age = False, gender = "Male"):
    if gender.lower() == "male":
        height = int(height.split(".")[0])*12 + int(height.split(".")[1])
        bmr = 66 + (6.3*weight) + (12.9*height) - (6.8*age)
        print("height:", height, "inches\n",bmr)

    if gender.lower() == "female":
        print("female")
print(random.randrange(1,4))