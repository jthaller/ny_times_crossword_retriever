# import bs4
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pyrobot import Robot
import os
# Selenium drivers to be installed to interact in order for selenium to work.
# Chrome:	https://sites.google.com/a/chromium.org/chromedriver/downloads
# Edge:	https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
# Firefox:	https://github.com/mozilla/geckodriver/releases
# Safari:	https://webkit.org/blog/6900/webdriver-support-in-safari-10/

# installing selenium webpage
# https://selenium-python.readthedocs.io/installation.html#introduction

# dealing with the print dialog
# https://stackoverflow.com/questions/11537103/how-to-handle-print-dialog-in-selenium


# this basically is everything lol
# https://stackoverflow.com/questions/26522739/how-to-click-on-the-print-button-on-a-web-page-using-selenium
website_url = 'https://www.seattletimes.com/games-nytimes-crossword/'
# driver = webdriver.Chrome()

driver = webdriver.Edge(executable_path="C:\\Users\\jerem\\Documents\\Python\\ny_times_crossword_retriever\\msedgedriver.exe")
driver = webdriver.Edge()
driver.get(website_url)
assert "NY Times Crossword | The Seattle Times" in driver.title
# print_button = a:contains('Print')

# --- click print button ---
printButton = driver.findElement(By.cssSelector("button.xwordjs-print-button"));
printButton.click();

# --- now a popup opens, click print again ---
# .....might need to add a line to wait for the action to finish.
printButton_popup = driver.findElement(By.cssSelector("button.btn-default"));
printButton_popup.click();

#now a new tab should open up with a pdf that needs to be printed
robot = Robot()


elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()
