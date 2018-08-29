#selenium & chrome(cli)
import sys
import io
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options #크롬 옵션 설정

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

chrome_options = Options()
chrome_options.add_argument("--headless") #크롬을 CLI 환경으로 실행

driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=r'D:/Atom_Workspace/section3/webdriver/chrome/chromedriver')
        #실행 옵션 및 path지정
#driver = webdriver.Chrome('D:/Atom_Workspace/section3/webdriver/chrome/chromedriver')
#driver.set_window_size(1920,1280)

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
