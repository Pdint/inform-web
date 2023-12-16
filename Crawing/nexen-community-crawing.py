from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
import re
import os

options = webdriver.ChromeOptions()
options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36')
options.add_argument("disable-images")
options.add_argument("--disable-default-image-capturing")

driver = webdriver.Chrome(options=options)

url = "https://forum.nexon.com/bluearchive/board_list?board=1018"
driver.get(url)
driver.maximize_window()

for i in range(1,18):
    if i == 6 or i == 11 or i == 16:
        page_butten = driver.find_element(By.XPATH, "//*[@id="next"]")
        page_butten.click()
    next_butten =  driver.find_element(By.ID, i )
    next_butten.click()
        
    time.sleep(5)
    for j in range(1, 16):
        text_list = []

        title = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[4]/div/ul/li["+ str(j) +"]/a/h3/span")
        title.click()
        driver.implicitly_wait(60)

        context = driver.find_elements(By.XPATH, "/html/body/div[1]/div/div[2]/div[3]/div[1]/div[1]/div/p")

        for x in context:
            text_list.append(x.text)
        text = " ".join(text_list)

        filename = driver.find_element(By.XPATH, '//*[@id="contents"]/div[2]/div/h3/span').text
        filename = re.sub(r'[\/:*?"<>|\n]', '', string=filename)
        file_path = os.path.join('Blue_Archive', filename + '.txt')
            
        with open(file_path,'w', encoding="utf-8") as flie:
            flie.write(text)

        driver.back()
        time.sleep(2)
        driver.implicitly_wait(60)
