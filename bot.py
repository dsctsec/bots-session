from selenium import webdriver
from bs4 import BeautifulSoup

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

URL = "https://google.com/"
query = "Covid 19 Worldometer"

# Get Chrome the Driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Call the URL
driver.get(URL)

# Find the Google Search Bar
search_box = driver.find_element("name", "q")
search_box.send_keys(query)

# Submit the search form
search_box.submit()

# Click on the first link
first_link = driver.find_element(By.CSS_SELECTOR, '#rso .g:first-child a')
first_link.click()


# Get the HTML of the page
html = driver.page_source

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Print the title of the pafe
print(soup.title)

# Find Data Elements
counter = soup.findAll(class_="maincounter-number")
counter1 = soup.findAll(class_="number-table-main")
counter2 = soup.findAll(class_="number-table")

# Parse Data Elements
total = counter[0].get_text().strip()
deaths = counter[1].get_text().strip()
recovered = counter[2].get_text().strip()

current = counter1[0].get_text().strip()
closed = counter1[1].get_text().strip()

deaths = counter2[3].get_text().strip()


# Print the Output
print("COVID 19 WORLD Updates")
print("TOTAL NUMBER OF CASES "+total)
print("TOTAL NUMBER OF ACTIVE CASES "+current)
print("TOTAL NUMBER OF DEATHS "+deaths)
print("TOTAL NUMBER OF RECOVERD PATIENTS "+recovered)
input()