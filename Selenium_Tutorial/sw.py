"""Permette di bloccare le richieste"""

from seleniumwire import webdriver  # Import from seleniumwire
from seleniumwire.utils import decode
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time
import json

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

def block_request(request):
    # Blocca PNG, JPEG e GIF
    if request.url.startswith('https://encrypted-tbn0.gstatic.com/images'):
        request.abort()

def mock_request(request):
    # Rimpiazza le richieste, in questo caso rimpiazza le immagini
    if request.url.startswith('https://encrypted-tbn0.gstatic.com/images'):
        request.create_response(
            status_code=200,
            headers={'Content-Type': 'image/jpeg'},  # Optional headers dictionary
                
            # Il body possiede un'immagine scaricata nel computer
            body=open("mountain.jpeg", "rb").read()
        )

# Se voglio bloccare un certo tipo di richieste:
#driver.request_interceptor = block_request

# Se voglio modificare un certo tipo di richieste:
driver.request_interceptor = mock_request


# Go to the Google home page
driver.get('https://www.google.com/search?q=wallpapers&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjxjJ_1iOn-AhWjRfEDHQ0OAJMQ_AUoAXoECAEQAw&biw=958&bih=915&dpr=1#imgrc=Ap8-_SDxuh-njM')

try:
    WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/div[1]/form[1]/div/div/button'))
        )
    driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/div[1]/form[1]/div/div/button').click()

except:
    pass

# Stampa tutti gli url che iniziano con quell'url
for request in driver.requests:
    if request.response:
        if request.url.startswith("https://encrypted-tbn0.gstatic.com/images"):
            print(request.url)

# Stampa in byte il contenuto dei JSON
for request in driver.requests:
    if request.response:
        if request.url.startswith("https://www.google.com/log?format=json"):
            body = request.response.body
            print(body)

# Stampa il contenuto leggibile dei JSON
for request in driver.requests:
    if request.response:
        if request.url.startswith("https://www.google.com/log?format=json"):
            response = request.response
            body = decode(response.body, response.headers.get('Content-Encoding', 'identity'))
            decoded_body = body.decode('utf-8') # rimuove la b iniziale
            json_data = json.loads(decoded_body)
            print(json_data)            