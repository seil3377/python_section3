import sys
import io
import requests

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#Response 상태코드
s = requests.Session()
r = s.get('http://httpbin.org/get')
print(r.status_code) # 200, 정상
print(r.ok) # true

#Json data handling
#https://jsonplaceholder.typicode.com

#r = s.get("https://jsonplaceholder.typicode.com/albums")
#print(r.text) # json 형태로가져옴

r = s.get("https://jsonplaceholder.typicode.com/posts/1")
#print(r.text)
print(r.json())
print(r.json().keys())
print(r.json().values())
print(r.encoding)
print(r.content) #컨텐츠의 형태 : 바이너리
print(r.raw)
