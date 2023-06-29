import time
from load_django import load

load()

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from parser_app.models import Links, Info


class info:

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

    def get_info(self):
        for i in Links.objects.values_list('links_on_hospital', flat=True):
            if i.startswith("https://doctor.webmd.com"):
                try:
                    print(i)
                    self.detour_cloudFlare(link=i)

                    name_hospital = self.driver.find_element(By.XPATH, "//h3[@class='facility-name']").text
                    print(name_hospital)
                    nuber_phone = self.driver.find_element(By.XPATH, '/html/body/div[1]/main/div/div[2]/div[2]/div/a/span/span/span[2]').text
                    print(nuber_phone)
                    overview = self.driver.find_element(By.XPATH, '//article').text
                    print(overview)
                    rating = self.driver.find_element(By.XPATH, "//div[@class='webmd-rate profile lhd-ratings loc-cr-ovrat']").get_attribute('aria-valuenow')
                    print(rating)
                    col_vo_reviews = self.driver.find_element(By.XPATH, "//span[@class='custom-review-count active-review-count']").text
                    print(col_vo_reviews)
                    bd_for_info = Info(name_hospital=name_hospital, number_phone=nuber_phone, overview=overview, ratings=rating, col_vo_reviews=col_vo_reviews)
                    bd_for_info.save()
                except:
                    pass
            else:
                print("not correct link")


C = info()
C.get_info()