import time
from selenium import webdriver
from bs4 import BeautifulSoup

# driver = webdriver.Chrome(ChromeDriverManager().install())
DRIVER_PATH = "/Python/ChromeDriver/chromedriver"
URL = "https://www.bcit.ca/study/programs/5512cert#courses"

browser = webdriver.Chrome(DRIVER_PATH)
browser.get(URL)

# Give the browser time to load all content.
time.sleep(3)

content = browser.find_elements_by_css_selector(".clicktoshow")
for e in content:
    start = e.get_attribute('innerHTML')
    # Beautiful soup allows us to remove HTML tags from our content if it exists.
    soup = BeautifulSoup(start, features="lxml")
    print(soup.get_text())
    print("***")  # Go to new line.
