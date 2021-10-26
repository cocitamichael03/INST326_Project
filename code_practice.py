import re
import urllib.request as url

def calculate_nutrients(weight, height, type):
    """Find website that takes parameters and returns the total nutrients needed."""
    web = url.urlopen("website")
    return 

def scrape():
    our_url = url.urlopen("https://www.livestrong.com/article/132010-general-nutritional-facts-about-chicken/")

    count = 0
    for line in our_url:
        line = line.decode("utf-8")
        #print(line)

class FoodNutrients:
    """The FoodNutrients class allows users to input food items
    and the quantity which is 1 by default.
    There is also an option for the user to input the weight of the food if know, otherwise,
    the default will be 100 grams when searched on the web. (Default weight)
    """

    def __init__(self, food, quantity = 1):
        self.food_lib = {}
        self.food = food
        self.quantity = quantity

    def find_nutrients(self, weight, height):
        self.weight = weight
        self.height = height
        self.type = input("Style: 1, 2, 3")
        self.total_nutrients = calculate_nutrients(self.weight, self.height, self.type)
        
    
    def add_food(self, food, quantity = 1):
        self.food = food
        self.quantity = quantity
    
    def scrape_web(self):
        for each in self.food:
            pass

    def get_total_intake(self):
        return f"Needed\nTotal fat: {}\nTotal carbs: {}\nTotal protein:\n"
    
    def get_food(self):
        number_items = len(self.food)
        count = 0
        while count < number_items:
            #print(self.quantity[count])
            #print(self.food[count])
            count += 1
            if self.food[count] not in self.food_lib:
                self.food_lib[self.food[count]] = self.quantity[count]
            else:
                self.food_lib[self.food[count]] += self.quantity[count]


meal1 = FoodNutrients(['egg', 'ham'], [2,1])
print(meal1.get_food())
