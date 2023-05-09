from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from twocaptcha import TwoCaptcha
import os
import time

browser = webdriver.Chrome()
browser.get("https://2captcha.com/demo/normal")

captcha_img = browser.find_element(By.CLASS_NAME, '_17bwEOs9gv8ZKqqYcEnMuQ')
captcha_img.screenshot('captcha.png')

api_key = os.getenv('APIKEY_2CAPTCHA', 'YOUR_API_KEY')

solver = TwoCaptcha(api_key)

try:
    result = solver.normal('captcha.png')

except Exception as e:
    print(e)

else:
    code = result['code']
    print(code)
    WebDriverWait(browser, 10).until(expected_conditions.presence_of_element_located((By.ID, 'simple-captcha-field')))
    browser.find_element(By.ID, 'simple-captcha-field').send_keys(code) # input field
    browser.find_element(By.CLASS_NAME, '')
    submit_button = browser.find_element(By.XPATH, '/html/body/div[1]/div/main/div/section/form/button[1]').click()

time.sleep(120)