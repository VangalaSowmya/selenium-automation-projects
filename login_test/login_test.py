#Login Test

from selenium import webdriver
from selenium.webdriver.common.by import By

# Start the browser
driver = webdriver.Chrome()

# Open the login page
driver.get("https://the-internet.herokuapp.com/login")

# Enter username and password
driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

# Click the login button
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# Print the login result
message = driver.find_element(By.ID, "flash").text
print("Login Message:", message)

# Close browser
driver.quit()
