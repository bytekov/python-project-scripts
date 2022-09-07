driver_location = "/home/baremetal/baremetals/chromedriver"

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.linkedin.com")

#========================= Login =========================#
sign_in_btn = driver.find_element(By.XPATH , '/html/body/nav/div/a[2]')
sign_in_btn.click()
mail_inpt = driver.find_element(By.XPATH , '//*[@id="username"]')
mail_inpt.send_keys("")
pass_inpt = driver.find_element(By.XPATH , '//*[@id="password"]')
pass_inpt.send_keys("")
log_in_btn = driver.find_element(By.XPATH , '//*[@id="organic-div"]/form/div[3]/button')
log_in_btn.click()

#========================= Make job search ===============#
search = driver.find_element(By.XPATH , '//*[@id="global-nav-typeahead"]/input')
search.send_keys("Php developer")
search.send_keys(Keys.RETURN)

import time
time.sleep(5)

#========================= Finish job application ============# 
forms = driver.find_element(By.XPATH , '//*[@id="forms"]')
pass_inpt.send_keys("My information")

apply_btn = driver.find_element(By.XPATH , '//*[@id="organic-div"]/form/div[3]/button')
apply_btn.click()







