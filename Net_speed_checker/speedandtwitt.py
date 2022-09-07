from socket import timeout
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Driver path
DRIVER_PATH = "/home/baremetal/baremetals/chromedriver"

class SpeedandTwitt:
    def __init__(self):
        # Opens controled chrome test browser
        self.driver = webdriver.Chrome(DRIVER_PATH)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.downspeed = 0
        self.upspeed = 0    
        #self.get_internet_speed()  
    
    # Test and get internet speed[upspeed/downspeed] in test browser 
    def get_internet_speed(self):
        self.driver.get("http://www.speedtest.net")
        
        self.driver.find_element(By.CLASS_NAME , "start-test").click()

        self.downspeed = self.driver.find_element(By.CLASS_NAME , "downspeed").text
        self.upspeed = self.driver.find_element(By.CLASS_NAME , "upspeed").text
    
    # Logs in to app=[twitter] , Create twitt , Forwards twitt
    def send_twitt(self):
        self.driver.find_element(By.CLASS_NAME , "create-twitt").click
        
        self.driver.get("http://www.twitter.com")
        user_mail = self.driver.find_element(By.CLASS_NAME , "mail")
        user_mail.send_keys("mytwitter")
        user_auth = self.driver.find_element(By.CLASS_NAME , "password")
        user_auth.send_keys("myauthentication")
        
        self.driver.find_element(By.CLASS_NAME , "login-button").click()
        
        twitt_message = f"Message here {self.upspeed} and {self.downspeed}"    
        twitt_form = self.driver.find_element(By.CLASS_NAME , "twitt-input")
        twitt_form.send_keys(twitt_message)
        
        self.driver.find_element(By.CLASS_NAME , "twitt-button").click
        
        