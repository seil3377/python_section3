#2.네이버 로그인 처리 후 회원 리스트 정보 가져오기
#3.Class Module 실습 작성
#4.자주 사용하는 Selenium 레퍼런스(Refference) 문서 훑어보기

import sys
import io
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class NcafeMenberExr:
    #초기화 실행(webdriver설정)
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless") #CLI (User-agent)
        self.driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="D:/Atom_Workspace/section3/webdriver/chrome/chromedriver")
        self.driver.implicitly_wait(5)

    # 카페회원 1페이지 정보 추출
    def getMemberList(self):
        self.driver.get('https://nid.naver.com/nidlogin.login')
        self.driver.find_element_by_name('id').send_keys('아이디입력')
        self.driver.find_element_by_name('pw').send_keys('비밀번호입력')
        self.driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
        self.driver.get('카페url')#cafeMemberView url을 Network탭에서 찾아준다
        self.driver.implicitly_wait(30)
        self.driver.switch_to_frame('cafe_main')
        self.driver.implicitly_wait(5)
        self.driver.switch_to_frame('innerframe')
        #print('test',self.driver.page_source)
        soup =BeautifulSoup(self.driver.page_source, 'html.parser')
        #print(soup.prettify())
        return soup.select('div.mem_wrap > div.mem_list div.ellipsis.m-tcol-c')

    #네이버 회원 리스트 출력 및 저장
    def printMenberList(self,list):
        f = open("D:/Atom_Workspace/section3/memberlist.txt",'wt')
        for i in list:
            f.wirte(i.string.strip()+"\n")
            print(i.string.strip())
        f.close()

    #소멸자
    def __del__(self):
        #self.driver.close() #현재 실행 포커스 된 영역을 종료
        self.driver.quit()  #Seleninum 전체 프로그램 종료
        print("Removed driver Object")

#실행영역
if __name__ == '__main__':
    #객체생성
    a = NcafeMenberExr(a.getMemberList())
    #시작
    start_time = time.time()
    #프로그램 측정
    a.printMenberList()
    #종료시간 출력
    print("---Total %s seconds ---" % (time.time() - start_time))
    #객체 소멸
    del a
