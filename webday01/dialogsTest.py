from selenium import webdriver
import time

#创建对象
dirver = webdriver.Chrome()

#获取网址
dirver.get("D:\python自动化资料\第1天\day01\资料\练习的html\练习的html\弹框的验证\dialogs.html")

#窗口变全屏
dirver.maximize_window()

#第一个按钮
dirver.find_element_by_id("alert").click()
time.sleep(3)
dirver.switch_to.alert.accept()
time.sleep(3)

#第二个按钮
dirver.find_element_by_id("confirm").click()
time.sleep(3)
dirver.switch_to.alert.accept()
time.sleep(3)
dirver.find_element_by_id("confirm").click()
time.sleep(3)
dirver.switch_to.alert.dismiss()
time.sleep(3)

dirver.quit()





dirver.quit()


















