#selenium & chrome
import sys
import io
from selenium import webdriver
import time

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

driver = webdriver.Chrome('D:/Atom_Workspace/section3/webdriver/chrome/chromedriver')
driver.set_window_size(1920,1280)

#driver.implicitly_wait(5)
driver.get("https://google.com")
time.sleep(5)
driver.save_screenshot("D:/Atom_Workspace/section3/website_ch1.png")

#driver.implicitly_wait(5)
driver.get('https://www.daum.net')
time.sleep(5)
driver.save_screenshot("D:/Atom_Workspace/section3/website_ch2.png")

driver.quit()

print("스크린샷 완료")
