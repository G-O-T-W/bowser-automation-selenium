from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os

# Define driver, options and service
chrome_options = Options()
chrome_options.page_load_strategy = 'none'
chrome_options.add_argument("--disable-search-engine-choice-screen")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

download_path = os.getcwd()
prefs = {'download.default_directory': download_path}
chrome_options.add_experimental_option('prefs', prefs)

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

# Locate elements dropdown and text box
elements = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div/div[1]/div/div/div[1]/span/div')))
elements.click()
text_box = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'item-0')))
text_box.click()

# Locate the form fields
fullname_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
email_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'userEmail')))
current_address_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'currentAddress')))
permanent_address_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'permanentAddress')))
submit_button = driver.find_element(By.ID, 'submit')

# Fill the form fields and click submit
fullname_field.send_keys("John Wick")
email_field.send_keys("johnwick@gmail.com")
current_address_field.send_keys("121 Mill Neck in Long Island, NY, USA")
permanent_address_field.send_keys("121 Mill Neck in Long Island, NY, USA")
driver.execute_script("arguments[0].click();", submit_button)

# Locate Upload and Download dropdown and the download button
upload_download = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'item-7')))
upload_download.click()
download_button = driver.find_element(By.ID, 'downloadButton')
driver.execute_script("arguments[0].click();", download_button)


input("Press enter to close the driver: ")
driver.quit()
