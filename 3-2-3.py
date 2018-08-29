import sys
import io
import requests, json

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

s = requests.Session()

r = s.get('http://httpbin.org/stream/20')
#print(r.text)
#print(r.json()) #파싱에러 발생 # stream형태
#print(r.encoding) #None

if r.encoding is None:
    r.encoding = 'utf-8'

for line in r.iter_lines(decode_unicode=True):
    #print(line)
    #print(json.loads(line))
    b = json.loads(line)
    print(type(b))
    print(b['origin'])
