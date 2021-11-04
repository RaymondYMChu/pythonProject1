import re
import time
from selenium import webdriver
from bs4 import BeautifulSoup

# driver = webdriver.Chrome(ChromeDriverManager().install())
DRIVER_PATH = "/Python/ChromeDriver/chromedriver"
URL = "https://vpl.bibliocommons.com/events/search/index"

browser = webdriver.Chrome(DRIVER_PATH)
browser.get(URL)

# Give the browser time to load all content.
time.sleep(3)

content = browser.find_elements_by_css_selector(".event-row-item")

for e in content:
    textContent = e.get_attribute('innerHTML')
    # Beautiful soup removes HTML tags from our content if it exists.
    soup = BeautifulSoup(textContent, features="lxml")
    rawString = soup.get_text().strip()

    # Remove hidden characters for tabs and new lines.
    rawString = re.sub(r"[\n\t]*", "", rawString)

    # Replace two or more consecutive empty spaces with '*'
    rawString = re.sub('[ ]{2,}', '*', rawString)

    # Fine tune the results so they can be parsed.
    #rawString = rawString.replace("Location", "Location*")
    #rawString = rawString.replace("Registration closed", "Registration closed*")
    #rawString = rawString.replace("Registration required", "Registration required*")
    #rawString = rawString.replace("In Progress", "*In Progress*")
    #rawString = rawString.replace("*/*", "/")
    #rawString = rawString.replace("Full*", "*Full*")


    print(rawString)
    print("***")

