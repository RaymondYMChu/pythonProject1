import re
import time
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

# driver = webdriver.Chrome(ChromeDriverManager().install())
DRIVER_PATH = "/Python/ChromeDriver/chromedriver"
URL = "https://www.bcliquorstores.com/"

browser = webdriver.Chrome(DRIVER_PATH)
browser.get(URL)

# Find the search input and send key of "Bordeaux"
search = browser.find_element_by_css_selector("#header-search")
search.send_keys("Bordeaux")

# Find the search button - this is only enabled when a search query is entered
button = browser.find_element_by_css_selector("#desktop-mag")
button.click()  # Click the button.

# Give the browser time to load all content.
time.sleep(3)

class LibraryWine:  # Declare class.
    # Declare and initialize wine property.
    wineName = ""
    wineVol = ""
    wineCountry = ""
    wineAvailability = ""
    wineFinalprice = ""
    wineOriginalprice=""

    # This is our constructor. It initializes variables when the object is created.
    def __init__(self, wineName, wineVol, wineCountry, wineAvailability, wineFinalprice, wineOriginalprice):
        self.wineName = wineName
        self.wineVol = wineVol
        self.wineCountry = wineCountry
        self.wineAvailability = wineAvailability
        self.wineFinalprice = wineFinalprice
        self.wineOriginalprice = wineOriginalprice
    # part e to loop thru the list and display in nicely formated manner
    def showDetail(self):
        print("Name:           " + self.wineName)
        print("Volume:         " + self.wineVol)
        print("Country:        " + self.wineCountry)
        print("Availability:   " + self.wineAvailability)
        print("Price:          " + self.wineFinalprice)
        print("Original Price: " + self.wineOriginalprice)
        print("***")

#create a empty list
wineList = []

# b) a loop to scrape 3 pages of the site
for i in range(0,3):
    def extractText(data):
        text = data.get_attribute('innerHTML')
        soup = BeautifulSoup(text, features="lxml")
        content = soup.get_text()
        return content

    products = browser.find_elements_by_css_selector(".product-description-container")

    for e in products: # d) Extracts text, parse and clean content from scraped content.
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
        rawString = rawString.replace("375 ml", "*750 ml*")
        rawString = rawString.replace("1.5 L", "*1.5 L*")
        rawString = rawString.replace("16 L", "*16 L*")
        rawString = rawString.replace("4 L", "*4 L*")
        rawString = rawString.replace("3 L", "*3 L*")
        rawString = rawString.replace("6 L", "*6 L*")
        rawString = rawString.replace("In Stock", "*In Stock")
        rawString = rawString.replace("$", "*$")
        rawString = rawString.replace("More Info", "*More Info")
        rawString = rawString.replace("Available", "*Available")
        rawString = rawString.replace("On Sale", "*On Sale")
        rawString = rawString.replace("until*", "until")

        #split the String by *
        eventArray = rawString.split('*')

        WINE_NAME = 0
        WINE_VOL = 1
        WINE_COUNTRY = 2
        WINE_AVAILABILITY = 3
        WINE_FINALPRICE = 4
        WINE_ORIGINALPRICE = 5

        wineName = eventArray[WINE_NAME]
        wineVol = eventArray[WINE_VOL].strip()  # remove leading and trailing spaces
        wineCountry = eventArray[WINE_COUNTRY].strip()  # remove leading and trailing spaces
        wineFinalprice = eventArray[WINE_FINALPRICE]
        wineAvailability = eventArray[WINE_AVAILABILITY]
        wineOriginalprice = eventArray[WINE_ORIGINALPRICE]

        # append Event to winelist
        wine = LibraryWine(wineName, wineVol, wineCountry, wineAvailability, wineFinalprice, wineOriginalprice)
        wineList.append(wine)

    button = browser.find_element_by_css_selector(".fa-caret-right")
    button.click()
    time.sleep(4)

# a loop to display wine list.
for wines in wineList:
    wines.showDetail()

#f) create an empty dataframe
dataSet = {'Name': [],'Volume':[],'Country': [],'Availability':[],'Price':[],'Original Price':[] }
df = pd.DataFrame(dataSet, columns= ['Name','Volume','Country','Availability','Price','Original Price'])

# f) build a data frame from wine list
for wines in wineList:
    dataSet2 = {'Name': [wines.wineName], 'Volume': [wines.wineVol], 'Country': [wines.wineCountry],
                              'Availability':[wines.wineAvailability],'Price':[wines.wineFinalprice],
                             'Original Price':[wines.wineOriginalprice] }
    dfAdd = pd.DataFrame(dataSet2, columns=['Name', 'Volume', 'Country', 'Availability', 'Price', 'Original Price'])
    df = df.append(dfAdd)

#create a dataframe and put into csv and then extract the final 2 rows from the csv
DRIVER_PATH        = "/Users/rchuy/OneDrive/Desktop/BCIT/COMP2454 Python/Dataset/"
CSV_FILE ='winelist.csv'

dfOut       = pd.DataFrame( data = df)
dfOut.to_csv(DRIVER_PATH + CSV_FILE, sep=',')

dfIn        = pd.read_csv(DRIVER_PATH + CSV_FILE, sep=',')
print(dfIn.tail(2))