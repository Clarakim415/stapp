import streamlit as st
import pandas as pd

# 타이틀, 헤더, 서브헤더
st.title('Title')
st.header('Title *Markdown* 인식')
st.subheader('Title *Markdown* 인식')

# 텍스트
st.text('title *Markdown* 인식 못함.')
st.markdown('***DataFrame*** 인식')

x = 10
y = 20
st.write('x = ', x, 'y = ', y)

df = pd.DataFrame({'col':[1,2,3]})
df
st.write('데이터 프레임', df)

import matplotlib.pyplot as plt
import numpy as np

# plot
arr = np.random.normal(1,1,size=100)
fig, ax = plt.subplots()
ax.hist(arr,bins=20)

fig

# 코드 블럭
code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language='python')

# 캡션 출력 & 이모지
st.caption('This')
st.caption('A  _italics_ :blue[colors]  :sunglasses:')

# Markdown 텍스트 컬러 적용
st.markdown('This is :blue[blue]')
st.markdown('This is :red[red]')

st.caption(':100:점~ :smile:')








