from selenium import webdriver
# For using sleep function because selenium
# works only when the all the elemets of the
# page is loaded.
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

Followlink= "https://www.zomato.com/users/hunger-dream-596167/network"
browser = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\chromedriver.exe")
browser.get(Followlink)

time.sleep(3)
username = "test"
password = "test"

# def check_exists_xpath(xpath):

browser.find_element_by_xpath("//a[@id='signin-link']").click()
time.sleep(2)
browser.find_element_by_xpath("//a[@id='login-email']").click()

a = browser.find_element_by_xpath("//input[@id='ld-email']")
a.send_keys(username)
b = browser.find_element_by_xpath("//input[@id='ld-password']")
b.send_keys(password)

browser.find_element_by_xpath("//input[@id='ld-submit-global']").click()

time.sleep(2)
i = 0
while True:
    try:
        button = browser.find_element_by_xpath(
            "//a[@class='snippet__follow social-button follow-social zs-follow-user-button']")
        browser.execute_script("return arguments[0].scrollIntoView();", button)
        button.click()
    # i+=1
    except:
        try:
            k = browser.find_element_by_xpath("//div[@class='load-more']")
            browser.execute_script("return arguments[0].scrollIntoView();", button)
            time.sleep(1)
            k.click()
        except:
            try:
                time.sleep(2)
                k = browser.find_element_by_xpath("//div[@class='load-more']")
                browser.execute_script("return arguments[0].scrollIntoView();", button)
                k.click()
            except:
                time.sleep(3)
                k = browser.find_element_by_xpath("//div[@class='load-more']")
                browser.execute_script("return arguments[0].scrollIntoView();", button)
                k.click()
