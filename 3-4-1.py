# 1.루리웹(Ruliweb) 사이트 로그인 처리 후 게시판 글 가져오기
# 2.인프런(Inflearn) 사이트 로그인 처리 후 개인정보 가져오기

import sys
import io
import requests
from bs4 import BeautifulSoup

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#어떤 request를 보내는가? : Request URL: http://user.ruliweb.com/member/login_proc
# form data: user_id, user_pw

# 로그인 유저정보
LOGIN_INFO = {
    'user_id': '아이디',
    'user_pw': '비밀번호'
}

#Session생성, with 구문 안에서 유지
with requests.Session() as s:
    login_req = s.post('http://user.ruliweb.com/member/login_proc', data=LOGIN_INFO)
    #HTML소스 확인
    #print('login_req'login_req.text)
    #Header 확인
    #print('headers', login_req.headers)
    if login_req.status_code == 200 and login_req.ok:
        post_one = s.get('http://market.ruliweb.com/read.htm?table=market_ps&page=1&num=4455742&find=&ftext=')
        post_one.raise_for_status() #예외 처리 발생시 처리
        soup = BeautifulSoup(post_one.text, 'html.parser')
        #print(soup.prettify())
        article = soup.select_one("table:nth-of-type(3)").find_all('p')
        #print(article)
        for i in article:
            if i.string is not None and i.img == None:
                print(i.string)
