from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep

user_pass={
    "user_name": ["mariam_flash@mail.ru", "login@mail.ru"],
    "pass_word": ["amer111", "eur111"]
}

user_list=user_pass.get("user_name")
pwd_list=user_pass.get("pass_word")

s=Service("C:\Selenium driver for Chrome\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://www.browserstack.com/users/sign_in")

driver.find_element(By.ID, "accept-cookie-notification").click()
sleep(1)

driver.find_element(By.ID, "user_email_login").send_keys(user_list[0])
driver.find_element(By.ID, "user_password").send_keys(pwd_list[0])

driver.find_element(By.CSS_SELECTOR, "input[type=\"submit\"]").click()

print("logged in successfully")














