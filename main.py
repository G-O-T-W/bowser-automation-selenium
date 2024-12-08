from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
# To remove the window for selecting search engine
chrome_options.add_argument("--disable-search-engine-choice-screen")
# To remove the certificate issues due to running in a sandboxed environment
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

service = Service('chromedriver-linux/chromedriver')
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get("https://demoqa.com/login")

input("Press enter to close the driver: ")
driver.quit()
