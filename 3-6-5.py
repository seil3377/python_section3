import sys
import io
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#chrome_options = Options()
#chrome_options.add_argument("--headless")

#driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=r'D:/Atom_Workspace/section3/webdriver/chrome/chromedriver')
driver = webdriver.Chrome('D:/Atom_Workspace/section3/webdriver/chrome/chromedriver')
driver.set_window_size(1920, 1280)
driver.implicitly_wait(3)

driver.get('https://www.inflearn.com/wp-login.php?redirect_to=https%3A%2F%2Fwww.inflearn.com%2F') #리다이렉트된 로그인 페이지
time.sleep(5)
driver.implicitly_wait(3)

driver.find_element_by_name('log').send_keys('id') #element의 name이 log인곳에 id를 보냄
driver.implicitly_wait(1)

driver.find_element_by_name('pwd').send_keys('pw')
driver.implicitly_wait(1)

# 로그인
driver.find_element_by_xpath('//*[@id="wp-submit"]').click() #클릭
