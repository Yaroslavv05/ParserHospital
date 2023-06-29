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
            name_cites = []
            links_hoshital = []
            self.detour_cloudFlare()

            name_category = self.driver.find_element(By.XPATH, f'/html/body/div[1]/div[2]/div[3]/ul/li[{i+1}]/a').text
            print(name_category)
            self.driver.find_element(By.XPATH, f'/html/body/div[1]/div[2]/div[3]/ul/li[{i+1}]').click()
            time.sleep(5)

            for j in range(28):
                link_hoshital = self.driver.find_element(By.XPATH, f'/html/body/div[1]/main/div[2]/div[1]/ul/li[{j+1}]/ul/li[1]/a').get_attribute('href')
                name_city = self.driver.find_element(By.XPATH, f'/html/body/div[1]/main/div[2]/div[1]/ul/li[{j+1}]/ul/li[1]/a').text
                name_cites.append(name_city)
                links_hoshital.append(link_hoshital)
                print(name_city)
                print(link_hoshital)
            name = ', '.join(name_cites)
            link = ', '.join(links_hoshital)
            bd_for_category = Category(name_category=name_category, cities=name, links_on_cities=link)
            bd_for_category.save()


C = category()
C.collection()