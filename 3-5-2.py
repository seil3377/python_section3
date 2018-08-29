# 1. 보안 토큰(csrf Token), Fake User-agent, Header Payload 처리
# 2. 위시캣(wishket) 사이트 로그인 처리 후 정보 가져오기
# Fake-UserAgent - https://pypi.python.org/pypi/fake-useragent

import requests
from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#요청 URL
URL = 'https://www.wishket.com/accounts/login/'

with requests.Session() as s:
    #URL연결
    s.get(URL)
    #Login 정보 Payload
    LOGIN_INFO = {
        'identification': '아이디',
        'password': '비밀번호',
        'csrfmiddlewaretoken': s.cookies['csrftoken']
    }
    print('token: ',s.cookies['csrftoken'])

    #요청
    response = s.post(URL, data=LOGIN_INFO)
    #HTML 결과 확인
    print('response',response.text)
        #forbidden 403 : 서버 거절, Referer header was not sent
