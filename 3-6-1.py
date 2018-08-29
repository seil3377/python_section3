#1. Selenium 개념 및 설치(크롬,파이어폭스)

#환경설정
#selenium + 크롬, 파이어폭스, PhantomJS
#운영체제에 맞는 Webdriver download

#selenium & phantomjs
import sys
import io
from selenium import webdriver

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

driver = webdriver.PhantomJS('D:/Atom_Workspace/section3/webdriver/phantomjs/bin/phantomjs')
'''
UserWarning: Selenium support for PhantomJS has been deprecated, please use headless versions of Chrome or Firefox instead
  warnings.warn('Selenium support for PhantomJS has been deprecated, please use headless '
'''  #셀레늄이 버전업이 되면서 PhantomJS를 지원하지 않으나 쓸만함(command line interface 환경 & 빠름)

driver.implicitly_wait(5)
driver.get("https://google.com")
driver.save_screenshot("D:/Atom_Workspace/section3/website1.png")

driver.implicitly_wait(5)
driver.get('https://www.daum.net')
driver.save_screenshot("D:/Atom_Workspace/section3/website2.png")

driver.quit()

print("스크린샷 완료")
