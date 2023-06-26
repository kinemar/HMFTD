# 라이브러리 파일 불러오기
import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# CSV 파일 읽어오기
File_path = './SGI관측소 제원정보.csv'

# SGI 변수에 File 경로 확립
SGI = pd.read_csv(File_path,encoding='cp949')

# SGI 변수를 재귀하고, 검출
SGI = SGI.T
SGI.head()

# DF_SGI 변수에 SGI중 필요한 데이터 추출 한 뒤 다시 재귀
df_SGI = SGI.iloc[[0,1]]
df_SGI = df_SGI.T
df_SGI.head()
# DF_SGI의 인덱스를 '관측소명'컬럼으로 변환
df_SGI = df_SGI.set_index(['관측소명'])
# DF_SGI 변수를 JSON로 다시 변환
df_SGI.to_json('./SGI관측소코드.json')
