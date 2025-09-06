from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch browser
driver = webdriver.Chrome()

# Open demo webshop
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()

# Click on "Books" category
driver.find_element(By.LINK_TEXT, "Books").click()

# Add first book to cart
driver.find_element(By.XPATH, "(//input[@value='Add to cart'])[1]").click()

# Wait for cart update
time.sleep(2)

# Go to shopping cart
driver.find_element(By.LINK_TEXT, "Shopping cart").click()

# Verify item in cart
item_name = driver.find_element(By.CLASS_NAME, "product-name").text
print("Item in cart:", item_name)

# Pause to view
time.sleep(3)

driver.quit()
