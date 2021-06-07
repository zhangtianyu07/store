from appium import webdriver
from selenium.webdriver import ActionChains
import time

#Appium Server端口默认为4723
server = r'http://localhost:4723/wd/hub'
desired_capabilities = {
    'platformName':'Android',
    'deviceName':'127.0.0.1:62001',
    'platformVersion':'7.1.2',
    'appPackage':'com.ss.android.ugc.aweme',
    'appActivity':'com.ss.android.ugc.aweme.splash.SplashActivity'
}
driver = webdriver.Remote(server,desired_capabilities)
time.sleep(3)
driver.tap([(448,970)],50)
time.sleep(2)
while True:

    time.sleep(5)
    start_x = 500
    start_y = 1300
    distance = 1000
    driver.swipe(start_x,start_y,start_x,start_y - distance)