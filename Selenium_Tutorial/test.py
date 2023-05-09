from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

browser = webdriver.Chrome()
browser.get(
    "https://www.amazon.it/s?k=mouse+gaming&i=stripbooks&rh=n%3A508733031&__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1682421754&ref=sr_pg_1" 
)

while True:
    pass