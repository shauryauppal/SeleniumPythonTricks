"""
Created on Mon Dec 25 01:49:47 2017

@author: shaur
"""
from selenium import webdriver
 # For using sleep function because selenium
# works only when the all the elemets of the
# page is loaded.
import time
browser = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\chromedriver.exe")

followlink = "https://www.instagram.com/abcd/"
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
time.sleep(1)
browser.get(followlink)
time.sleep(3)

browser.find_element_by_xpath("//li[@class='_bnq48'][2]/a[1]").click()

try:
    button = browser.find_element_by_xpath("//div[@class='_o0j5z']/div[1]/div[1]/ul[1]/div[1]/li[1][4]/div[1]/div[1]/span[1]/button[1]")
    button.click()
except:
    button = browser.find_element_by_xpath("//li[@class='_6e4x5'][4]/div[1]/div[1]/span[1]/button[1]")
    button.click()
