# Decode A Web Page    
# This is the first 4-chili exercise of this blog! We’ll see what people think, and decide whether or not to continue with 4-chili exercises in the future.

# Exercise 17 (and Solution)
# Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.

import requests
import bs4
from bs4 import BeautifulSoup


target_link = "https://www.nytimes.com"

response = requests.get(url=target_link)
response_html = response.text

doc = BeautifulSoup(response_html, 'html.parser')

articles = doc.find_all(class_='e1lsht870')

for x in articles:
    print(x.string)

