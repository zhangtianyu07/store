from selenium import webdriver

import time

dirver = webdriver.Chrome()

dirver.get("D:\python自动化资料\第1天\day01\资料\练习的html\练习的html\跳转页面\pop.html")

dirver.maximize_window()

dirver.find_element_by_id("goo").click()

time.sleep(5)

dirver.quit()







