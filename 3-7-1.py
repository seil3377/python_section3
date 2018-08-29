#1.Selenium을 이용한 네이버 카페 자동으로 글쓰기

import sys
import io
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class NcafeWriteAtt:
    #초기화 실행(webdriver설정)
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless") #CLI (User-agent)
        self.driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="D:/Atom_Workspace/section3/webdriver/chrome/chromedriver")
        self.driver.implicitly_wait(5)

    #로그인 & 출석체크
    def writeAttendCheck(self):
        self.driver.get('https://nid.naver.com/nidlogin.login')
        self.driver.find_element_by_name('id').send_keys('아이디입력')
        self.driver.find_element_by_name('pw').send_keys('비밀번호입력')
        self.driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
        self.driver.implicitly_wait(10) #response대기
        self.driver.get('카페url')#실질적으로 url이 바뀌지 않고 ajax처리 되는 페이지는 개발자 도구 네트워크 탭에서 찾아준다.
        self.driver.implicitly_wait(10)
        self.driver.switch_to_frame('cafe_main') #iframe의 값을 가져오는 method
        self.driver.find_element_by_id('cmtinput').send_keys('반갑습니다!') #textarea에 키값을 보냄
        self.driver.find_element_by_xpath('//*[@id="main-area"]/div[6]/table/tbody/tr[4]/td/table/tbody/tr/td[3]/a/img').click()
        time.sleep(3)

    #소멸자
    def __del__(self):
        #self.driver.close() #현재 실행 포커스 된 영역을 종료
        self.driver.quit()  #Seleninum 전체 프로그램 종료
        print("Removed driver Object")

#실행영역
if __name__ == '__main__':
    #객체생성
    a = NcafeWriteAtt()
    #시작
    start_time = time.time()
    #프로그램 측정
    a.writeAttendCheck()
    #종료시간 출력
    print("---Total %s seconds ---" % (time.time() - start_time))
    #객체 소멸
    del a
