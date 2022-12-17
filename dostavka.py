from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from fake_useragent import UserAgent as UA
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import randint


ua = UA(browsers='chrome')

driver_service = Service(executable_path=r'C:\Users\37533\Desktop\dostavka\dostavka\chromedriver\chromedriver.exe')
options = webdriver.ChromeOptions()
options.add_argument(f'user-agent={ua}')
driver = webdriver.Chrome(service=driver_service)
driver.maximize_window()

#url = 'https://edostavka.by/login?screen=withPassword'
url = 'https://edostavka.by/login?screen=phone'
#url = 'https://vk.com'
try:
    driver.get(url=url)
    # accept coockies
    driver.find_element(By.XPATH,"//button[@class='button button_size_medium button_type_subtle accept-cookies_accept__mok-Y']").click()
    time.sleep(randint(2,5))
    # change login mode to with password
    driver.find_element(By.XPATH, "//button[@class='button button_size_large button_type_subtle phone_button__2Z9fs phone_button__padding__e0VFd']").click()
    time.sleep(randint(2,5))
    # type phone number
    driver.find_element(By.XPATH, "//input[@class='index-module_wrapperPhone__input__KD5gF']").send_keys('292146098')
    time.sleep(randint(2,5))
    # type password
    driver.find_element(By.XPATH, "//input[@class='input__input input__input_size_medium']").send_keys('Tinker100500')
    time.sleep(randint(2,5))
    driver.find_element(By.XPATH, "//button[@class='button button_size_large button_type_primary withPassword_button__1xJLn']").click()
    time.sleep(5)
    print('qwe')

except Exception as e:
    print(e)
finally:
    driver.close()
    driver.quit()