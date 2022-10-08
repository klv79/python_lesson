from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import time
from pymongo import MongoClient
import pprint
import pandas

#client = MongoClient('127.0.0.1', 27017)
#db = client['mvideo_trend']
#trends_db = db.mvideo_trends


s = Service('./chromedriver')
driver = webdriver.Chrome(service=s)
driver.get('https://www.mvideo.ru/')
time.sleep(5)
driver.execute_script("window.scrollTo(0, window.scrollY + 1500)")
time.sleep(5)
#buttons = driver.find_elements(By.CLASS_NAME, 'tab-button')

#time.sleep(10)
#scroll = driver.find_element(By.CLASS_NAME, 'title__text')
#scroll.click()
trend = driver.find_element(By.XPATH, "//span[contains(text(), ' В тренде ')]")
col = driver.find_element(By.XPATH, "//span[contains(text(), ' 16 ')]")
#print(col.text)
trend.click()

buttons = driver.find_elements(By.CLASS_NAME, 'tab-button')

button_trend = buttons[1]
button_trend.click()
trends = driver.find_element(By.XPATH, "//mvid-shelf-group[@class='page-carousel-padding ng-star-inserted']")
while True:
    try:
        # wait = WebDriverWait(driver, 15)
        button_next = trends.find_element(By.XPATH, "//mvid-carousel[@class='carusel ng-star-inserted']//"
                                                "button[@class='btn forward mv-icon-button--primary mv-icon-button--shadow mv-icon-button--medium mv-button mv-icon-button']")
        # button_next = wait.until(EC.element_to_be_clickable((By.XPATH, "//mvid-carousel[@class='carusel ng-star-inserted']//"
        #                                                                                   "button[@class='btn forward mv-icon-button--primary mv-icon-button--shadow mv-icon-button--medium mv-button mv-icon-button']")))

        button_next.click()

    except:
        break
i = 1
#goods = trends.find_elements(By.CLASS_NAME, 'title')
goods = buttons[0].find_elements(By.XPATH, "./ancestor::mvid-shelf-group")
names = goods[0].find_elements(By.XPATH, "//div[@class='title']")
names1 = trends.find_elements(By.XPATH, "//div[@class='product-mini-card__name ng-star-inserted']")
#item = {}
item_list = []
i = 1
for name in names1:
    item = {
        'name': name.text

    }
    #item['name'] = name.text
    #print(i)
    #print(item)
    i = i + 1
    item_list.append(item)
    if i == int(col.text) + 1:
        break
    #trends_db.insert_one(item)

driver.quit()
#print(item_list)
print(pandas.DataFrame(item_list))

#while EC.presence_of_all_elements_located((By.LINK_TEXT, 'В тренде')):
 #   scroll.send_keys(Keys.DOWN)
  #  time.sleep(10)






