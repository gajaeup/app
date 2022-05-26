from calendar import month
import requests
from bs4 import BeautifulSoup
from datetime import datetime

location = input("지역을 입력하세요\n>>> ")
a = []
Finallocation = location + '날씨' 
LocationInfo = "" 
NowTemp = "" 
url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=' + Finallocation 
hdr = {'User-Agent': ('mozilla/5.0 (windows nt 10.0; win64; x64) applewebkit/537.36 (khtml, like gecko) chrome/78.0.3904.70 safari/537.36')} 
req = requests.get(url, headers=hdr) 
html = req.text 
soup = BeautifulSoup(html, 'html.parser') 
Month = datetime.today().month
Month = str(Month)
# 오류 체크 
ErrorCheck = soup.find('span', {'class' : 'btn_select'})
if 'None' in str(Finallocation): 
    print(text = "Error! 지역 검색 오류!") 
else: 
    # 지역 정보 
    for i in soup.select('span[class=btn_select]'): 
        LocationInfo = i.text     
    NowTemp = soup.find(class_='temperature_text')
    temp = NowTemp.text
    temp = float(temp.strip(' 현재온도°'))
    temp = int(temp)
    weather= soup.find(class_='weather before_slash')


    print(temp)
    print(weather.text)

if '눈' in str(weather):
    a.append('눈')
    print(a)
if '1' in str(weather):
    a.append('눈')
if '2' in str(weather):
    a.append('눈')
if '비' in str(weather):
    a.append('비')    
    print(a)
if '흐림' in str(weather):
    a.append('흐림')
    print(a)
if '맑음' in str(weather):
    a.append('맑음')
    print(a)



            


