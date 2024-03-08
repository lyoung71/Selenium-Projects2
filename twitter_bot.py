import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException


options = Options()
options.add_argument("user-data-dir=/tmp/tarun")

driver = webdriver.Chrome(
    '/Users/landonyoung/Downloads/chromedriver-mac-arm64/chromedriver',
    options=options
    )
driver.get('https://twitter.com')
driver.implicitly_wait(10)

hashmap = {}

emoji_list = [
    'Face with open mouth',
    'Clown face',
    'Grinning face with smiling eyes',
    'Smiling face with open mouth and smiling eyes',
    'Partying face',
    'Cowboy hat face',
    'Face with monocle',
    'Disguised face',
    'Nerd face',
    'Smiling face with sunglasses'
]

try:
    count = 0

    while count < 10:
        emoji = emoji_list[count]
        tweet_elem = driver.find_element(
            By.CLASS_NAME,
            "DraftEditor-editorContainer"
            ).click()
        add_emoji = driver.find_element(
            By.XPATH,
            "//div[@aria-label='Add emoji']"
            ).click()
        add_emoji = driver.find_element(
            By.XPATH,
            f"//div[@aria-label='{emoji}']"
            ).click()
        root = driver.find_element(By.ID, "react-root").click()
        post_elem = driver.find_element(
            By.XPATH,
            "//div[@data-testid='tweetButtonInline']"
            ).click()
        count += 1
        time.sleep(60)

    time.sleep(3)

except NoSuchElementException:
    username = input("What is your username?")
    password = input("What is your password?")
    email = input("What is your email?")
    driver.get('https://twitter.com/i/flow/login')
    email_elem = driver.find_element(
        By.XPATH,
        "//input[@autocomplete='username']"
        )
    email_elem.send_keys(f"{email}", Keys.ENTER)
    time.sleep(3)

    username_elem = driver.find_element(
        By.XPATH,
        "//input[@autocomplete='on']"
        )
    username_elem.send_keys(username, Keys.ENTER)
    driver.implicitly_wait(5)

    password_elem = driver.find_element(
        By.XPATH,
        "//input[@autocomplete='current-password']"
        )
    password_elem.send_keys(password, Keys.ENTER)
    time.sleep(3)
