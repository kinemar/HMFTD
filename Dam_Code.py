# 라이브러리 임포트
import requests
import pandas as pd
from pandas import DataFrame
import urllib.request
import xml
import pprint
import json
from pandas import json_normalize

 # 공공데이터 가져오기 5
url = 'http://opendata.kwater.or.kr/openapi-data/service/pubd/dam/droughtInfo/damcode/list'
params ={'serviceKey' : 'tuwIomWD+mLLnOWnnCuHWnRkHymc81TXs/JDnOQcmbJFmPE9998K8yNVZoJ68P/QfW1mayal69eYQmt1abGO5A=='
         , 'numOfRows' : '100'
         , 'pageNo' : '1'
         , '_type' : 'json'}
response = requests.get(url, params=params)
contents = response.text         

# json 데이터 dataframe으로 변환
json_ob = json.loads(contents)
body = json_ob['response']['body']['items']['item']
df = json_normalize(body)
print(df)

# dataframe을 슬라이싱
dataF = df.iloc[1:]
dataF = dataF.T
dataF = dataF.loc[['damnm','damcode']]
dataF = dataF.T

# dataF를 csv파일로
dataF.to_csv('fucking_Dam.csv')
