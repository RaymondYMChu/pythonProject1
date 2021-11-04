import time
import re
from selenium import webdriver
from bs4 import BeautifulSoup

# driver = webdriver.Chrome(ChromeDriverManager().install())
DRIVER_PATH = "/Python/ChromeDriver/chromedriver"
URL = "https://animalfactguide.com/links/"

browser = webdriver.Chrome(DRIVER_PATH)
browser.get(URL)

time.sleep(3)

# Find the search input.
search = browser.find_element_by_css_selector("#s")
search.send_keys("Zebra")

# Find the search button - this is only enabled when a search query is entered
button = browser.find_element_by_css_selector("#searchsubmit")
button.click()  # Click the button.

# Extracts text from scraped content.
def extractText(data):
    text    = data.get_attribute('innerHTML')
    soup    = BeautifulSoup(text, features="lxml")
    content = soup.get_text()
    return content

titles       = browser.find_elements_by_css_selector(".entry-title a")
descriptions = browser.find_elements_by_css_selector(".entry-summary p")

titleList       = []
descriptionList = []

for i in range(0, len(titles)):
    # extract title and add to list.
    title       = extractText(titles[i])
    titleList.append(title)

    # extract description and add to list.
    description = extractText(descriptions[i])
    descriptionList.append(description)

# Show the content.
for i in range(0, len(descriptionList)):
    print("\n********************")
    print("Title:       " + titleList[i])
    print("Description: " + descriptionList[i])
