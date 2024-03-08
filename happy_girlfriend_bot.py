import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("user-data-dir=/tmp/tarun")

driver = webdriver.Chrome(
    '/Users/landonyoung/Downloads/chromedriver-mac-arm64/chromedriver',
    options=options
    )
driver.get('https://web.whatsapp.com/')
driver.implicitly_wait(15)
time.sleep(10)
now = datetime.now()

if now.hour <= 23 and now.hour >= 18:
    message = "Boa noite, amor \nColinho de noite"
elif now.hour < 18 and now.hour >= 12:
    message = "Boa tarde, amor \nColinho de tarde"
else:
    message = "Bom dia, amor \nColinho de manha"

amor_elem = driver.find_element(By.XPATH, "//span[@title='Juliana♌']").click()
message_elem = driver.find_element(By.XPATH, "//div[@title='Type a message']")
message_elem.send_keys(message, Keys.SPACE, ":kiss", Keys.ENTER, Keys.ENTER)
time.sleep(40)
