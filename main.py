from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import nexmo
import time
import os
import datetime

url = 'https://www.nike.com/launch/?s=in-stock'
driver = webdriver.Chrome('/Users/loganvaleski/Desktop/Python/snkrs_monitor/chromedriver')
driver.get(url)

# toggle grid view
wait = WebDriverWait(driver, 5)
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Show Products as List']"))).click();

# datetime stuff
cur_time = datetime.datetime.utcnow().strftime("%H:%M:%S")

# wait for shoes to drop
while driver.find_element_by_xpath("//div[@class='figcaption-content']//h3[contains(.,'MOON RACER')]"):
    os.system("clear")
    print(cur_time,":", "SNKR has not dropped")
    time.sleep(120)
    driver.get(url)
    cur_time = datetime.datetime.utcnow().strftime("%H:%M:%S")

# message and loop end
os.system("clear")
print(cur_time,":", "SNKR has dropped")

NEXMO_KEY = os.environ.get('NEXMO_KEY')
NEXMO_SECRET = os.environ.get('NEXMO_SECRET')

client = nexmo.Client(key=NEXMO_KEY, secret=NEXMO_SECRET)

response = client.send_message({'from' : '18444398499', 'to' : '17202561768', 'text' : 'Check SNKRS.'})

response = response['messages'][0]

if response['status'] == '0':
    print ('Send message ', response['message-id'])
else:
    print ('Error: ', response['error-text'])
