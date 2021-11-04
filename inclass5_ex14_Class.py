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

class LibraryEvent:  # Declare class.
    # Declare and initialize age property.
    eventName = ""
    eventDate = ""
    eventTime = ""
    eventLocation = ""

    # This is our constructor. It initializes variables when the object is created.
    def __init__(self, eventName, eventDate, eventTime, eventLocation):
        self.eventName = eventName
        self.eventDate = eventDate
        self.eventTime = eventTime
        self.eventLocation = eventLocation
    #
    def showDetail(self):
        print("Name:     " + self.eventName)
        print("Date:     " + self.eventDate)
        print("Time:     " + self.eventTime)
        print("Location: " + self.eventLocation)
        print("***")

eventList = []

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
    rawString = rawString.replace("Location", "Location*")
    rawString = rawString.replace("Registration closed", "Registration closed*")
    rawString = rawString.replace("Registration required", "Registration required*")
    rawString = rawString.replace("In Progress", "*In Progress*")
    rawString = rawString.replace("*/*", "/")
    rawString = rawString.replace("Full*", "*Full*")
    # print(rawString)
    eventArray = rawString.split('*')

    EVENT_NAME = 0
    EVENT_DATE = 1
    EVENT_TIME = 2
    eventName = eventArray[EVENT_NAME]
    eventDate = eventArray[EVENT_DATE].strip()  # remove leading and trailing spaces
    eventTime = eventArray[EVENT_TIME].strip()  # remove leading and trailing spaces
    eventLocation = eventArray[len(eventArray) - 1]
    # append Event to eventlist
    event = LibraryEvent(eventName,eventDate, eventTime, eventLocation)
    eventList.append(event)
print(eventList)
    # Declare a function to display details about the child.

# We can easily display object detail without concern for the internal data & logic.
for events in eventList:
    events.showDetail()
