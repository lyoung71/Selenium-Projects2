from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


password = input("Enter password: ")
recipient = input("Please enter recipient of message: ")

browser = webdriver.Chrome('/Users/landonyoung/Downloads/chromedriver-mac-arm64/chromedriver')
browser.get('https://www.google.com/gmail/about/')
sign_in = browser.find_element(By.LINK_TEXT, "Sign in")
sign_in.click()

email_elem = browser.find_element(By.ID, 'identifierId')
email_elem.send_keys('seleniumtesttt@gmail.com')
email_elem.send_keys(Keys.ENTER)

captcha = input("Please enter the captcha: ")
captcha_elem = browser.find_element(By.ID, 'ca')
captcha_elem.click()
captcha_elem.send_keys(captcha)
captcha_elem.send_keys(Keys.ENTER)

browser.implicitly_wait(3)
password_elem = browser.find_element(By.XPATH, '//*[@id="password"]//input')
password_elem.send_keys(password)
password_elem.send_keys(Keys.ENTER)

compose_button = browser.find_element(By.XPATH, '/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div/div')
compose_button.click()

browser.implicitly_wait(1)
to_elem = browser.find_element(By.ID, ':bq')
to_elem.send_keys(recipient)

browser.implicitly_wait(1)
subject_elem = browser.find_element(By.NAME, 'subjectbox')
subject_elem.send_keys('This is a test')

message_elem = browser.find_element(By.ID, ':9e')
message_elem.send_keys("I used a bot to send this to you.")

send_elem = browser.find_element(By.ID, ':7u')
send_elem.click()
