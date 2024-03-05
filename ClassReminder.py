from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException



options = Options()
options.add_argument("user-data-dir=/tmp/tarun")

driver = webdriver.Chrome('/Users/landonyoung/Downloads/chromedriver-mac-arm64/chromedriver', options=options)
driver.get("https://preply.com/en/calendar")

today = datetime.now()
todayString = today.strftime('%Y-%m-%d')
print(todayString)
schedule = []
message = "Today\'s schedule: \n"

try:
    driver.implicitly_wait(10)
    class_elems = driver.find_elements(By.XPATH, f"//td[@data-date='{todayString}']//span[@class='fc-event-title']")
    time_elems = driver.find_elements(By.XPATH, f"//td[@data-date='{todayString}']//span[@class='fc-event-time']")
    for i in range(len(class_elems)):
        schedule.append(f"{class_elems[i].text} ({time_elems[i].text})")
    for item in schedule:
        message += f"{item}\n"
    print(message)

    driver.get('https://web.whatsapp.com/')
    driver.implicitly_wait(30)
    me_elem = driver.find_element(By.XPATH, "//span[@title='Eu']").click()
    message_elem = driver.find_element(By.XPATH, "//div[@title='Type a message']")
    message_elem.send_keys(message, Keys.ENTER)


except NoSuchElementException:
    print('No classes scheduled for today.')
