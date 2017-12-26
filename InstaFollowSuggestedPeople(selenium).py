"""
Created on Mon Dec 25 01:49:47 2017

@author: shaur
"""
from selenium import webdriver     
 # For using sleep function because selenium 
# works only when the all the elemets of the 
# page is loaded.
import time   
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import random
browser = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\chromedriver.exe") 

followlink = "https://www.instagram.com/thegreatindianfoodie/"
username ="test"
password="test"
browser.get(followlink)
time.sleep(2)

browser.find_element_by_xpath("//a[@class='_l8p4s'][2]").click()
time.sleep(2)

a = browser.find_element_by_xpath("//div[@class='_t296e'][1]/div[1]/input[1]")
a.send_keys(username)

b = browser.find_element_by_xpath("//div[@class='_t296e'][2]/div[1]/input[1]")
b.send_keys(password)

browser.find_element_by_xpath("//button[@class='_qv64e _gexxb _4tgw8 _njrw0']").click()
time.sleep(2)
browser.get("https://www.instagram.com/explore/people")
time.sleep(3)

k=0
while True:
    for i in range(1,21):
        path = '//*[@id="react-root"]/section/main/div/ul/div/li[' + str(i) + ']/div/div[1]/div[2]/span/button'
        c = browser.find_element_by_xpath(path)
            #browser.execute_script("return arguments[0].scrollIntoView();", c)
        x = random.randint(1,70)
        time.sleep(2+x%7)
        c.send_keys(Keys.ENTER)
    
    k = random.randint(4,200)
    time.sleep(10+k%101)
    browser.implicitly_wait(10+k%97)
    browser.get("https://www.instagram.com/explore/people")
    time.sleep(10+k%101)
    browser.implicitly_wait(10+k%97)