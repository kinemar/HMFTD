# 라이브러리 불러오기
import os
import sys
import requests
import datetime
import time
import json
import pandas as pd

# json파일 읽기
SGI_JSON = pd.read_json('./SGI관측소코드.json')

#서비스키
ServiceKey = 'R58VCxkxdFAOTRXshGROm1MT2zZvY1JqAdRYVG70zr8GFjUpdGpA2I7gwrbKE7FG%2Fnh0K1ej7RpcI9wxBMfyyg%3D%3D&   '

#URL 작성
APICODE = 'http://apis.data.go.kr/B500001/drghtSGIIdex_20211020?serviceKey=' + ServiceKey

Page_NO = input('몇 페이지를 확인할까요? : ')
APICODE = APICODE + '&pageNo=' + Page_NO 

NOR = input('한 페이지에 얼마의 결과를 출력할까요? : ')
APICODE = APICODE + 'numOfRows=' + NOR 

df = SGI_JSON.loc[[input('어느 관측소에서의 정보를 얻어올까요? : ')]]
df['관측소코드'] = df['관측소코드'].astype(str)
df = df.values
APICODE = APICODE + '&obsrvtCd=' + df 

Year = str(input('몇년도 기록을 확인할까요?(yyyy) : '))
Month = str(input('몇월달 기록을 확인할까요?(mm) : '))
Start = Year + Month + '01&'
if(Month == ('01' or '03' or '05' or '07' or '08' or '10' or '12')):
  End = Year + Month + '31&'
elif(Month == '02'):
  End = Year + Month + '28&'
else: End = Year + Month + '30&'
APICODE = APICODE + 'stDt=' + Start + 'edDt=' + End

_TYPECODE = input('어떤 파일 형식으로 출력할까요? (xml/json) : ')
APICODE = APICODE + '_type=' + _TYPECODE

API_RQ = requests.get(APICODE)
