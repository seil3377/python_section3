import sys
import io
import requests, json

#Rest : POST보내기, GET가져오기, PUT업데이트&교체, FETCH업데이트&모디파이, DELETE삭제하기

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

payload1 = {'key1':'value1', 'key2':'value2'}
payload2 = (('key1','value1'),('key2','value2'))
payload3 = {'some':'nice'}

#r = requests.put('http://httpbin.org/user/delete', data=payload1)
#print(r.text)

#r = requests.put('https://jsonplaceholder.typicode.com/posts/1',data=payload1)
#print(r.text)

#r = requests.put('https://github.com/user/put', data=payload1)
#print(r.text)

r = requests.delete('https://jsonplaceholder.typicode.com/posts/1')
print(r.text)
