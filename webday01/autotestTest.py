from selenium import webdriver
import time

#创建对象
dirver = webdriver.Chrome()

#获取网页地址
dirver.get(r"D:\python自动化资料\第1天\day01\资料\练习的html\练习的html\上传文件和下拉列表\\autotest.html")

#窗口全屏
dirver.maximize_window()

#获取输入框传送值
dirver.find_element_by_xpath("//*[@id = 'accountID']").send_keys("123456789")
dirver.find_element_by_xpath("//*[@id = 'passwordID']").send_keys("123456")
dirver.find_element_by_xpath("//*[@id = 'areaID']").send_keys("天津市")
dirver.find_element_by_xpath("//*[@id = 'sexID1']").click()
dirver.find_element_by_xpath("//*[@value = 'spring']").click()
dirver.find_element_by_xpath("//*[@value = 'winter']").click()
dirver.find_element_by_xpath("//input[@name = 'file' and @type = 'file']").send_keys("D:\python自动化资料\第1天\day01\资料\练习的html\练习的html\上传文件和下拉列表\呸.jpg")
dirver.find_element_by_xpath("//*[@id = 'buttonID']").click()

time.sleep(3)

dirver.quit()


















