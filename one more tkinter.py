from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import tkinter as tk
import time
from fake_useragent import UserAgent as UA


def search_result():
    bot = webdriver.Chrome()
    ua = UA(browsers='chrome')
    driver_service = Service(executable_path=r'C:\Users\37533\Desktop\dostavka\dostavka\chromedriver\chromedriver.exe')
    options = webdriver.ChromeOptions()
    options.add_argument(f'user-agent={ua}')

    bot.get('https://google.com')
    time.sleep(3)
    window.quit()
    result = bot.find_element(By.NAME, 'q')
    result.clear()
    result.send_keys(entry1.get())
    result.send_keys(Keys.RETURN)
def facebook():
    print('')

window = tk.Tk()
window.geometry('450x200')
search=tk.Label(window, text='what are you finding?', font='times 15')
search.place(x=10,y=10)
entry1 = tk.Entry(window)
entry1.place(x=250, y=10)

b1=tk.Button(window,text='search', command=search_result, width=12, bg='gray')
b1.place(x=150,y=50)

b2=tk.Button(window,text='Facebook', command=facebook, width=12, bg='gray')
b2.place(x=150,y=100)

window.tk.mainloop()




