# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time 


# Use uc.Chrome() instead of standard webdriver.Chrome()
driver = uc.Chrome(version_main=144)

driver.get("https://google.com")
time.sleep(2)

# Fetch the Search Input Box using Xpath

user_input= driver.find_element(by=By.XPATH,value='//*[@id="APjFqb"]')
user_input.send_keys('Campus X')
time.sleep(2)

user_input.send_keys(Keys.ENTER)
time.sleep(15) 

link= driver.find_element(by=By.XPATH,value='//*[@id="_6JaXafq4GvPhkdUPlKTZqAU_37"]')
link.click()
time.sleep(3)

print("Success!")

# ADD THIS LINE TO FIX THE ERROR
driver.quit()