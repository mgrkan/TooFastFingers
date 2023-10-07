import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

DRIVER_PATH = "./chromedriver"

options = Options()

service = Service(executable_path=DRIVER_PATH)
driver = webdriver.Chrome(options=options, service=service)

driver.get("https://10fastfingers.com/typing-test/turkish")


deny = driver.find_element(By.ID, "CybotCookiebotDialogBodyButtonDecline")
deny.click()
#words = driver.find_elements(By.ID, "row1")
#print(len(words))
#words = words[0].text
#print(words)
#words = words.split(" ")
#print(words)
text_input = driver.find_element(By.ID, "inputfield")
for i in range(1, 500):
    word = driver.find_element(By.CLASS_NAME, "highlight")
    word = word.text
    text_input.send_keys(word)
    text_input.send_keys(Keys.SPACE)
time.sleep(20)

