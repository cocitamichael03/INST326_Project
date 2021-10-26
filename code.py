import re
import urllib.request as url

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

    def __init__(self, food, quantity = 1 , weight = 100):
        self.food = food
        self.quantity = quantity

    def scrape_web(self):
        for each in self.food:
            pass

    def get_total_intake(self):
        return f""
    
    def get_food(self):
        number_items = len(self.food)
        count = 0
        while count < number_items:
            print(self.food[count])
        
        return self.food[0], number_items

meal1 = FoodNutrients(['egg', 'ham'], 2)
print(meal1.get_food())





# total_intake = 23g pro, 5g fat, 10g carbs

# total_day = 30g pro, 15g fat, 30g carbs

# needed = 7g pro, 10g fat, 20g carbs


