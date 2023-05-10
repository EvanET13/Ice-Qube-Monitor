import time
import re
import requests
import colorama
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from colorama import Fore

color1 = Fore.LIGHTYELLOW_EX
color2 = Fore.MAGENTA
color3 = Fore.LIGHTCYAN_EX

url = input("Enter IceQube IP:  "+ color3)
urlpage = "http://" + url 


print(color2 + "Parsing Temperature Data from: " + urlpage)
# run chrome webdriver from executable path of your choice
driver = webdriver.Chrome()

# get web page
driver.get(urlpage)
time.sleep(2)

page = requests.get(urlpage)
time.sleep(2)
soup = BeautifulSoup(page.content,"html.parser")


pls = driver.find_element(By.XPATH, '//*[@id="txtTemperatures"]').text

tempInFar = re.search(r'\d+', pls)


if int(tempInFar[0]) >= 100:                            # made element of list an int() because parsed value is a str
    print(color1 + "\n\n1:temp:"+str(tempInFar[0])+"\n\n")
else:
    print(color1 + "\n\n0:temp:"+str(tempInFar[0])+"\n\n")

