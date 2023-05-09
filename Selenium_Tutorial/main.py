from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import json
from pathlib import Path

browser = webdriver.Chrome()
browser.get(
    "https://www.amazon.it/s?k=mouse+gaming&i=stripbooks&rh=n%3A508733031&__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1682421754&ref=sr_pg_1"
)

path = Path("D:\\Coding\\Python\\Selenium_Tutorial\\data.txt")
data = Path("D:\\Coding\\Python\\Selenium_Tutorial\\data.json")


def write_json(new_data):
    with data.open("r+") as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data.append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent=4)


def write_data(title, price, img, link):
    with path.open("a+") as f:
        f.write(f"Title: {title}\n")
        f.write(f"Price: {price}\n")
        f.write(f"Img: {img}\n")
        f.write(f"Link: {link}\n\n")


def checkCookies():
    try:
        WebDriverWait(browser, 10).until(
            expected_conditions.presence_of_element_located((By.ID, "sp-cc-accept"))
        )
        browser.find_element(By.ID, "sp-cc-accept").click()
    except:
        print("Can't find cookie button")


def getProduct(items):
    for item in items:
        try:
            title = item.find_element(By.TAG_NAME, "h2").text
            print("Title: " + title)
        except:
            title = "No title"
            print("Can't read title")

        try:
            price = item.find_element(By.CLASS_NAME, "a-price-whole").text
            print("Price: " + price + " €")
        except:
            price = "No price"
            print("Price doesn't exist")

        try:
            img = item.find_element(By.CSS_SELECTOR, ".s-image").get_attribute("src")
            print("Image url: " + img)
        except:
            img = "No img"
            print("Error with img url")

        try:
            link = item.find_element(By.CLASS_NAME, "a-link-normal").get_attribute(
                "href"
            )
            print("Product link: " + link)
        except:
            link = "No link"
            print("Can't find product link")

        print("\n")

        # write_data(title, price, img, link)
        write_json({"Title": title, "Price": price, "Img": img, "Link": link})


def nextPage():
    try:
        next_btn = WebDriverWait(browser, 10).until(
            expected_conditions.presence_of_element_located(
                (By.CLASS_NAME, "s-pagination-next")
            )
        )

        if "s-pagination-disabled" in next_btn.get_attribute("class"):
            isNextDisabled = True
        else:
            browser.find_element(By.CLASS_NAME, "s-pagination-next").click()

        return isNextDisabled

    except:
        pass


def closeApp():
    close = input("Exit program (y/N): ")
    if close == "y":
        browser.close()
        exit()


def main():
    with data.open("w") as f:
        json.dump([], f)

    global isNextDisabled
    isNextDisabled = False

    checkCookies()

    while not isNextDisabled:
        try:
            WebDriverWait(browser, 10).until(
                expected_conditions.presence_of_element_located(
                    (By.XPATH, '//div[@data-component-type="s-search-result"]')
                )
            )

            elem_list = browser.find_element(
                By.CSS_SELECTOR, "div.s-main-slot.s-result-list.s-search-results.sg-row"
            )  # tasto destro, copy selector

            items = elem_list.find_elements(
                By.XPATH, '//div[@data-component-type="s-search-result"]'
            )

            # print(len(items))

            getProduct(items)

            if nextPage() == True:
                break

        except Exception as e:
            print(e, "Main error")
            isNextDisabled = True

    closeApp()


if __name__ == "__main__":
    main()
