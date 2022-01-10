# Decode A Web Page Two    
# Exercise 19 (and Solution)
# Using the requests and BeautifulSoup Python libraries, print to the screen the full text of the article on this website: http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture.

# The article is long, so it is split up between 4 pages. Your task is to print out the text to the screen so that you can read the full article without having to click any buttons.

# (Hint: The post here describes in detail how to use the BeautifulSoup and requests libraries through the solution of the exercise posted here.)

# This will just print the full text of the article to the screen. It will not make it easy to read, so next exercise we will learn how to write this text to a .txt file.

import requests
from bs4 import BeautifulSoup

link = "https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture"


connect = requests.get(url=link)

start_connect = connect.text

html_parser = BeautifulSoup(start_connect, 'html.parser')

header = html_parser.find(class_= "jgNsQT")

print(header.string)
print("---------------------------------")
paragraph = html_parser.find("div", class_= "body__inner-container")

print(paragraph.text)
print("---------------------------------")
next_paragraph = html_parser.find_all("p")

print(next_paragraph)