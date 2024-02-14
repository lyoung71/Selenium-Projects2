import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

options = Options()
options.add_argument("user-data-dir=/tmp/tarun")

email_address = input("What is your email address?")
password = input("Enter password: ")
recipient = input("Please enter recipient of message: ")

browser = webdriver.Chrome('/Users/landonyoung/Downloads/chromedriver-mac-arm64/chromedriver')
browser.get('https://www.google.com/gmail/about/')
sign_in = browser.find_element(By.LINK_TEXT, "Sign in")
sign_in.click()

email_elem = browser.find_element(By.ID, 'identifierId')
email_elem.send_keys(f'{email_address}')
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

try:
    browser.implicitly_wait(8)
    compose_button = browser.find_element(By.XPATH, '/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div/div')
    compose_button.click()
    browser.implicitly_wait(8)

    to_elem = browser.find_element(By.XPATH, "//input[@aria-label='To recipients']")
    to_elem.send_keys(recipient)
    browser.implicitly_wait(8)

    subject_elem = browser.find_element(By.NAME, 'subjectbox')
    subject_elem.send_keys('This is a test')
    browser.implicitly_wait(8)

    message_elem = browser.find_element(By.XPATH, "//div[@aria-label='Message Body']")
    message_elem.send_keys("I used a bot to send this to you.", Keys.TAB, Keys.ENTER)
    time.sleep(5)
    
except NoSuchElementException:
    verification_method_elem = browser.find_element(By.XPATH, "//div[@data-challengeid='3']").click()

    code = input("What is the verification code?")
    code_elem = browser.find_element(By.XPATH, "//div[@aria-label='Enter code']").send_keys()
    browser.implicitly_wait(8)
    compose_button = browser.find_element(By.XPATH, '/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div/div')
    compose_button.click()
    browser.implicitly_wait(8)

    to_elem = browser.find_element(By.XPATH, "//input[@aria-label='To recipients']")
    to_elem.send_keys(recipient)
    browser.implicitly_wait(8)

    subject_elem = browser.find_element(By.NAME, 'subjectbox')
    subject_elem.send_keys('This is a test')
    browser.implicitly_wait(8)

    message_elem = browser.find_element(By.XPATH, "//div[@aria-label='Message Body']")
    message_elem.send_keys("I used a bot to send this to you.", Keys.TAB, Keys.ENTER)
    time.sleep(5)
