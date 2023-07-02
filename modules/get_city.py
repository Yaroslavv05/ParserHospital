import time
from load_django import load

load()

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from parser_app.models import Category, City


class city:

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
        for i in Category.objects.all():
            link = i.link
            print(link)
            self.detour_cloudFlare(link)

            for j in range(28):
                name_city = self.driver.find_element(By.XPATH, f'/html/body/div[1]/main/div[2]/div[1]/ul/li[{j+1}]/ul/li[1]/a').text
                print(name_city)
                link_city = self.driver.find_element(By.XPATH, f'/html/body/div[1]/main/div[2]/div[1]/ul/li[{j+1}]/ul/li[1]/a').get_attribute('href')
                print(link_city)
                bd_for_city = City(category=link.replace('https://doctor.webmd.com/choice-awards/', ''), name=name_city, link=link_city, status='New')
                bd_for_city.save()


C = city()
C.get_links()