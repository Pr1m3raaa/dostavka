from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from fake_useragent import UserAgent as ua
from parser import q

ua = ua(browsers='chrome')

driver_service = Service(executable_path=r'C:\Users\37533\Desktop\dostavka\dostavka\chromedriver\chromedriver.exe')
options = webdriver.ChromeOptions()
#options.add_argument('user-agent=Chrome/53.0.2785.116 Safari/537.36 OPR/40.0.2308.81')
options.add_argument('user-agent=Chrome/53.0.2785.116 Safari/537.36 OPR/40.0.2308.81')
driver = webdriver.Chrome(service=driver_service)

#url = 'https://edostavka.by/login?screen=withPassword'
url = 'https://edostavka.by/login?screen=account'

try:
    driver.get(url=url)
    time.sleep(10)
    driver.find_element(By.CLASS_NAME,'button button_size_large button_type_subtle phone_button__2Z9fs phone_button__padding__e0VFd').click()
    time.sleep(5)
except Exception as e:
    print(e)
finally:
    driver.close()
    driver.quit()