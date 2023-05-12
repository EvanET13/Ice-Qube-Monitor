import time
import re
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from colorama import Fore
####### Not necessary for the code, just to beautify #######
default = Fore.RESET
color1 = Fore.LIGHTGREEN_EX
color2 = Fore.MAGENTA
color3 = Fore.LIGHTCYAN_EX
color4 = Fore.RED
############################################################

url = input("Enter IceQube IP:  "+ color3)
tempThresh = input(default + "What is the MAX temperature you want to allow: " + color3)
urlpage = "http://" + url 


print(color2 + "Parsing Temperature Data from: " + color3 + urlpage + color2 + " with MAX temperature set to: " + color3 + tempThresh)
# run chrome webdriver from executable path of your choice
driver = webdriver.Chrome()

# get web page
driver.get(urlpage)
time.sleep(2)

page = requests.get(urlpage)
time.sleep(2)
soup = BeautifulSoup(page.content,"html.parser")

##### added an indefinite loop to constantly check the temperature given there is a 2 second interval to allow time for temperature to change #####
while True:
    pls = driver.find_element(By.XPATH, '//*[@id="txtTemperatures"]').text
    time.sleep(2)
    tempInFar = re.search(r'\d+', pls)
    if int(tempInFar[0]) >= int(tempThresh):                            
        print(color4 + "\n\n1:temp:"+str(tempInFar[0])+"\n\n")
    else:
        print(color1 + "\n\n0:temp:"+str(tempInFar[0])+"\n\n")
    time.sleep(2)
    

