import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from solveRecaptcha import solveRecaptcha

browser = webdriver.Chrome()
browser.get("https://www.google.com/recaptcha/api2/demo")

result = solveRecaptcha(
    "6LfD3PIbAAAAAJs_eEHvoOl75_83eXSqpPSRFJ_u",
    "https://www.google.com/recaptcha/api2/demo",
)

code = result["code"]

WebDriverWait(browser, 10).until(
    expected_conditions.presence_of_element_located((By.ID, "recaptcha-anchor"))
)

browser.execute_script(
    "document.getElementById('g-recaptcha-response).innerHTML = " + "'" + code + "'"
)

browser.find_element(By.ID, "recaptcha-demo-submit").click()
