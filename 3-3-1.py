# 1. requests 모듈 사용법(2)
# 2. requests 모듈 Rest API 실습

import sys
import io
import requests, json

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


#r = requests.get('https://api.github.com/events')
#r.raise_for_status()# 에러가 발생했을 때 예외처리
                    # raise HTTPError(http_error_msg, response=self)
                    # requests.exceptions.HTTPError: 404 Client Error: Not Found for url: https://api.github.com/event
#print(r.text)

#------------------------------------------------------------------------------------------------------------------------
jar = requests.cookies.RequestsCookieJar()
jar.set("name","kim",domain="httpbin.org",path='/cookies') #키&벨류, 도메인과 쿠키경로를 세팅

r = requests.get('http://httpbin.org/cookies',cookies=jar)
r.raise_for_status()
print(r.text)

#우리가 보낸 값이 response됨
'''
{
  "cookies": {
    "name": "kim"
  }
}
'''
#------------------------------------------------------------------------------------------------------------------------
r = requests.get('https://github.com',timeout=5) #5초 대기
print(r.text)

#------------------------------------------------------------------------------------------------------------------------
#fake rest(test)
r = requests.post('http://httpbin.org/post', data={'name':'kim'}, cookies=jar)
print(r.text)

#------------------------------------------------------------------------------------------------------------------------
#form 데이터로 보냄
payload1 = {'key1':'value1', 'key2':'value2'} #dict
payload2 = (('key1','value1'),('key2','value2')) #tuple

r = requests.post('http://httpbin.org/post', data=payload1)
print(r.text)

r = requests.post('http://httpbin.org/post', data=payload2) #결과 데이터는 같다
print(r.text)

#------------------------------------------------------------------------------------------------------------------------
#json 형태로 보냄
payload3 = {'some':'nice'}
r = requests.post('http://httpbin.org/post', data=json.dumps(payload3))
print(r.text)
