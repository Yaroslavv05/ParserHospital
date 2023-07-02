import time
from load_django import load

load()

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from parser_app.models import Category


class category:

    def __init__(self):
        self.driver = uc.Chrome()

    def detour_cloudFlare(self):
        self.driver.get('https://doctor.webmd.com/choice-awards')
        time.sleep(10)

        try:
            self.driver.find_element(By.XPATH, "//iframe[@sandbox='allow-same-origin allow-scripts allow-popups']").click()
            time.sleep(10)
        except:
            print('Not cloudFlare')

    def collection(self):
        for i in range(5):
            self.detour_cloudFlare()

            name_category = self.driver.find_element(By.XPATH, f'/html/body/div[1]/div[2]/div[3]/ul/li[{i+1}]/a').text
            print(name_category)
            link = self.driver.find_element(By.XPATH, f'/html/body/div[1]/div[2]/div[3]/ul/li[{i+1}]/a').get_attribute('href')
            print(link)
            bd_for_category = Category(name_category=name_category, link=link, status='New')
            bd_for_category.save()


C = category()
C.collection()