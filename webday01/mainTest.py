from selenium import webdriver
import time
dirver = webdriver.Chrome()
dirver.get("D:\python自动化资料\第1天\day01\资料\练习的html\练习的html\\frame.html")
dirver.maximize_window()
dirver.find_element_by_id("input1").send_keys("123456789")
time.sleep(5)
dirver.quit()












