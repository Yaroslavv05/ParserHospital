import time
from load_django import load

load()

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from parser_app.models import Category, Links


class Link:

    def __init__(self):
        self.driver = uc.Chrome()

    def detour_cloudFlare(self, link):
            self.driver.get(link)
            time.sleep(10)

            try:
                self.driver.find_element(By.XPATH, "//iframe[@sandbox='allow-same-origin allow-scripts allow-popups']").click()
                time.sleep(10)
            except:
                print('Not cloudFlare')

    def get_links(self):
        for i in Category.objects.values_list('links_on_cities', flat=True)[0].split():
            self.detour_cloudFlare(link=i.replace(',', ''))

            for j in range(3):
                try:
                    links_hospital = self.driver.find_element(By.XPATH, f'/html/body/div[1]/main/div[2]/div[1]/div[1]/div[{j+1}]/div/div/div[2]/a').get_attribute('href')
                    bd_for_links = Links(links_on_hospital=links_hospital)
                    bd_for_links.save()
                except:
                    print('<3')


C = Link()
C.get_links()