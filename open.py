from selenium import webdriver
import time

dr=webdriver.Chrome()
print 'open chrome'
#time.sleep(2)

#dr.maximize_window()
dr.set_window_size(640,480)

time.sleep(2)
dr.quit()
print 'closed chrome'
