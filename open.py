from selenium import webdriver
import time

dr=webdriver.Chrome()
print 'open chrome'
time.sleep(2)

#dr.maximize_window()

time.sleep(2)
dr.quit()
print 'closed chrome'
