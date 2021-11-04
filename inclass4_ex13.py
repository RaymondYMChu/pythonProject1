import time
from selenium import webdriver
from bs4 import BeautifulSoup

# driver = webdriver.Chrome(ChromeDriverManager().install())
DRIVER_PATH = "/Python/ChromeDriver/chromedriver"
browser = None

# This loads webdriver from the local machine if it exists.
try:
    browser = webdriver.Chrome(DRIVER_PATH)
    print("The path to webdriver_manager was found.")

# If a webdriver not found error occurs it is then downloaded.
except:
    print("webdriver not found. Update 'DRIVER_PATH' with file path in the download.")
    browser = webdriver.Chrome(ChromeDriverManager().install())
