#form_test

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Start the browser
driver = webdriver.Chrome()

# Open the form page
driver.get("https://www.techlistic.com/p/selenium-practice-form.html")
driver.maximize_window()

# Fill in text fields
driver.find_element(By.NAME, "firstname").send_keys("Sowmya")
driver.find_element(By.NAME, "lastname").send_keys("Reddy")

# Select gender
driver.find_element(By.ID, "sex-1").click()

# Select years of experience
driver.find_element(By.ID, "exp-2").click()

# Enter date
driver.find_element(By.ID, "datepicker").send_keys("05-09-2025")

# Select profession
driver.find_element(By.ID, "profession-1").click()

# Select automation tool
driver.find_element(By.ID, "tool-2").click()

# Select continent from dropdown
continent = Select(driver.find_element(By.ID, "continents"))
continent.select_by_visible_text("Asia")

# Pause for observation
time.sleep(3)

print("Form filled successfully!")

# Close browser
driver.quit()
