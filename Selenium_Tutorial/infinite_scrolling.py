from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import json
import time

browser = webdriver.Chrome()
browser.get("https://intoli.com/blog/scrape-infinite-scroll/demo.html")

items = []  # Creiamo una lista vuota in cui salviamo gli elementi

last_height = browser.execute_script("return document.body.scrollHeight")

# Settiamo un numero massimo di elementi che possiamo scrollare
itemTargetCount = 100

while itemTargetCount > len(items):
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    
    time.sleep(1)   # ogni volta che arriviamo alla fine della pagina scrollando
                    # dobbiamo dare allo script del tempo per caricare gli elementi

    new_height = browser.execute_script("return document.body.scrollHeight")

    if new_height == last_height:
        break

    last_height = new_height

    elements = browser.find_elements(By.CSS_SELECTOR, "#boxes > div")
    textElements = []
    for element in elements:
        textElements.append(element.text)
        
    items = textElements

print(items)
print(f"Length: {len(items)}")

json.dump(items, open("items.json", "w"))