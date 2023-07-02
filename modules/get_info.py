import time
from load_django import load

load()

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from parser_app.models import ClinicLink, ClinicInfo


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
        for i in ClinicLink.objects.all():
            if i.link.startswith("https://doctor.webmd.com"):
                try:
                    print(i.link)
                    self.detour_cloudFlare(link=i.link)

                    name_hospital = self.driver.find_element(By.XPATH, "//h3[@class='facility-name']").text
                    print(name_hospital)
                    city = self.driver.find_element(By.XPATH, "//span[@class='facility-location-address']").text
                    print(city)
                    practicing_physicians_count = self.driver.find_element(By.XPATH, "//a[@class='practicing-physician-info']").text.replace('Practicing Physicians', '')
                    print(practicing_physicians_count)
                    rating = self.driver.find_element(By.XPATH, "//div[@class='webmd-rate profile lhd-ratings loc-cr-ovrat']").get_attribute('aria-valuenow')
                    print(rating)
                    address = self.driver.find_element(By.XPATH, "//span[@class='facility-location-address']").text
                    print(address)
                    phone_number = self.driver.find_element(By.XPATH, '/html/body/div[1]/main/div/div[2]/div[2]/div/a/span/span/span[2]').text
                    print(phone_number)
                    overview = self.driver.find_element(By.XPATH, '//article').text
                    print(overview)
                    bd_for_info = ClinicInfo(name=name_hospital, city=city, practicing_physicians_count=practicing_physicians_count, address=address, number_phone=phone_number, overview=overview)
                    bd_for_info.save()
                except Exception as ex:
                   print(ex)
            else:
                print("not correct link")


C = info()
C.get_info()