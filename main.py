from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Define driver, options and service
chrome_options = Options()
chrome_options.page_load_strategy = 'none'
chrome_options.add_argument("--disable-search-engine-choice-screen")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
service = Service('chromedriver-linux/chromedriver')
driver = webdriver.Chrome(service=service, options=chrome_options)

# Load the webpage
driver.get("https://demoqa.com/login")

# Locate username, password and login buttons
username_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'userName')))
password_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'password')))
login_button = driver.find_element(By.ID, 'login')

# Fill username, password and click login button
username_field.send_keys("pythoncourse")
password_field.send_keys("Ghont@x2208")
driver.execute_script("arguments[0].click();", login_button)

input("Press enter to close the driver: ")
driver.quit()
