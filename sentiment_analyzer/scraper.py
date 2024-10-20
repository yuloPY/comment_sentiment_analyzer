from selenium import webdriver
import time
import csv
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# URL of the youtube video to be scraped
url = "https://www.youtube.com/"

# WebDriver path
service = Service(r"your directory\geckodriver.exe")

# Start Firefox browser
driver = webdriver.Firefox(service=service)

# Open Youtube video page
driver.get(url)

# Wait for the comments section to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#comments")))

# Scroll the comments section
driver.execute_script("window.scrollTo(0, 500);")
time.sleep(7)

# Continue scrolling to load more comments
last_height = driver.execute_script("return document.documentElement.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    time.sleep(3)
    new_height = driver.execute_script("return document.documentElement.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# Find comments
comments = driver.find_elements(By.CSS_SELECTOR, "#content-text")

# Define the filename and path
filename = r"your directory\comments.csv"

# Save comments to a CSV file
with open(filename, mode='a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['comments'])
    for comment in comments:
        writer.writerow([comment.text])

# Close the browser
driver.quit()
