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

#for i in range(1, 500):
#    word = driver.find_element(By.CLASS_NAME, "highlight")
#    word = word.text
#    text_input.send_keys(word)
#    text_input.send_keys(Keys.SPACE)
words = []
i = -1
while True:
    i += 1
    el = "//span[@wordnr='{}']".format(i)
    print(el)
    try:
        word = driver.find_element(By.XPATH, el)
        driver.execute_script("arguments[0].scrollIntoView();", word)
        print(word, word.text)
        words.append(word.text)
    except:
        word = driver.find_element(By.XPATH, "//span[@wordnr='1']")
        driver.execute_script("arguments[0].scrollIntoView();", word)
        break
text_input = driver.find_element(By.ID, "inputfield")
for i in words:
    text_input.send_keys(i)
    text_input.send_keys(Keys.SPACE)

time.sleep(20)

