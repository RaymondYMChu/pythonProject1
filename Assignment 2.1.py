import re
import time
from selenium import webdriver
from bs4 import BeautifulSoup

# driver = webdriver.Chrome(ChromeDriverManager().install())
DRIVER_PATH = "/Python/ChromeDriver/chromedriver"
URL = "https://www.coursera.org/"

browser = webdriver.Chrome(DRIVER_PATH)
browser.get(URL)

# Give the browser time to load all content.
time.sleep(3)

# Find the search input.
search = browser.find_element_by_css_selector(".react-autosuggest__input")
search.send_keys("data analytics")

# Find the search button - this is only enabled when a search query is entered
button = browser.find_element_by_css_selector(".search-form")
button.click()  # Click the button.

# Extracts text from scraped content.
def extractText(data):
    text    = data.get_attribute('innerHTML')
    soup    = BeautifulSoup(text, features="lxml")
    content = soup.get_text()
    return content

courses       = browser.find_elements_by_css_selector(".product-description-container")

#productList       = []

#for i in range(0, len(products)):
    # extract title and add to list.
 #   product       = extractText(products[i])
  #  productList.append(product)

for e in courses:
    textContent = e.get_attribute('innerHTML')
    # Beautiful soup removes HTML tags from our content if it exists.
    soup = BeautifulSoup(textContent, features="lxml")
    rawString = soup.get_text().strip()

    # Remove hidden characters for tabs and new lines.
    rawString = re.sub(r"[\n\t]*", "", rawString)
    # Replace two or more consecutive empty spaces with '*'
    rawString = re.sub('[ ]{2,}', '*', rawString)


    # Fine tune the results so they can be parsed.
    rawString = rawString.replace("750 ml", "*750 ml*")
    rawString = rawString.replace("1.5 L", "*1.5 L*")
    rawString = rawString.replace("In Stock", "*In Stock")
    rawString = rawString.replace("$","*$")
    rawString = rawString.replace("More Info", "*More Info")
    rawString = rawString.replace("until*", "until")
    print(rawString)
 #   eventArray = rawString.split('*')

  #  WINE_NAME = 0
   # WINE_VOL = 1
    #WINE_COUNTRY = 2
    #WINE_AVAILABILITY = 3
    #WINE_PRICE = 4
    #WINE_DIS = 5

    #wineName = eventArray[WINE_NAME]
    #wineVol = eventArray[WINE_VOL].strip()  # remove leading and trailing spaces
    #wineCountry = eventArray[WINE_COUNTRY].strip()  # remove leading and trailing spaces
    #winePrice = eventArray[WINE_PRICE]
    #wineAvailability = eventArray[WINE_AVAILABILITY]
    #wineDis = eventArray[WINE_DIS]

    #print("Name:     " + wineName)
    #print("Volume:     " + wineVol)
    #print("Country:     " + wineCountry)
    #print("Availability:     " + wineAvailability)
    #print("Price:     " + winePrice)
    #print("Price if there is discount:     " + wineDis)
    #print("***")