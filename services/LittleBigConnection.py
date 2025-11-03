from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

CHROMIUM_PATH = "/usr/bin/chromium"
CHROMEDRIVER_PATH = "/usr/bin/chromedriver"

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.binary_location = CHROMIUM_PATH

service = Service(CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://app.connecting-expertise.com/supplier/supplierrequest/list")
print(driver.title)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
print(soup)
for a in soup.find_all("a"):
    print(a.get_text(strip=True), "=>", a.get("href"))

driver.quit()
