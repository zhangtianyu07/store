from selenium import webdriver
import time

#创建对象
driver = webdriver.Chrome()

#获取网址
driver.get(r"D:\python自动化资料\第1天\day01\资料\练习的html\练习的html\main.html")

#窗口最大化
driver.maximize_window()

#获取最外层位置
driver.switch_to.frame("frame")

#获取输入框发送一个值
driver.find_element_by_id("input1").send_keys("123456")

#时间
time.sleep(5)

#关闭
driver.quit()





















