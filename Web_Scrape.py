import re
import urllib.request as url
#https://www.livestrong.com/article/132010-general-nutritional-facts-about-chicken/

our_url = url.urlopen("https://www.livestrong.com/article/132010-general-nutritional-facts-about-chicken/")

count = 0
for line in our_url:
    line = line.decode("utf-8")
    print(line)
    #