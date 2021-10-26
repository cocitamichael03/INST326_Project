import re
import urllib.request as url

def scrape():
    our_url = url.urlopen("https://www.livestrong.com/article/132010-general-nutritional-facts-about-chicken/")

    count = 0
    for line in our_url:
        line = line.decode("utf-8")
        #print(line)




class FoodNutrients:
    def __init__(self, food, quantity = 1 , weight = 100)
        self.food = food
        pass

    def scrape_web(self):
        for each in food:
            pass

    
    
    def get_total_intake(self):
        return f""





# total_intake = 23g pro, 5g fat, 10g carbs

# total_day = 30g pro, 15g fat, 30g carbs

# needed = 7g pro, 10g fat, 20g carbs


