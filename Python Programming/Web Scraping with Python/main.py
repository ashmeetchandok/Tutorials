#-------------------------------------------------#
# Here we are scraping the Flipkart Website.
# We are scraping for the best laptop on Flipkart
#-------------------------------------------------#

#-- Importing Libraries --#
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

#-- Selenium Plugin used for automating Chrome--#
driver = webdriver.Chrome()


#---------------------------------------------------#
# Now we are going to extract the import information
# such as the name, price and rating of the product
#---------------------------------------------------#

#-- Variables for storing --#
products = []
prices = []
ratings = []

#-- Accessing the page and storing the content --#
driver.get('https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&sort=popularity')
content = driver.page_source

#-- Beautiful Soup --#
soup = BeautifulSoup(content)
for i in soup.findAll('a',href=True,attrs={'class':'_31qSD5'}): #class names extracted from inspect element
    name = i.find('div', attrs={'class':'_3wU53n'})
    price = i.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
    rating = i.find('div', attrs={'class':'hGSR34'})
    
    #appending the entries to list.
    products.append(name.text)
    prices.append(price.text)
    ratings.append(rating.text)


#-- Saving it into an excel file using Pandas --#
df = pd.DataFrame({'Product Name':products,'Price':prices,'Rating':ratings}) 
df.to_csv('webscrapper.csv', index=False, encoding='utf-8')



