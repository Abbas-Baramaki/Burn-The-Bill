from selenium import webdriver
from selenium.webdriver.chrome.options import Options

proxy = "41.59.65.202:80"

chrome_options = Options()
chrome_options.add_argument(f'--proxy-server={proxy}')

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://httpbin.org/ip")  # سایت ساده برای تست پروکسی

input("Press Enter to exit...")
driver.quit()
