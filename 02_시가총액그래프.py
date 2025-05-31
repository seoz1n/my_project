import streamlit as st
import plotly.graph_objs as go
import pandas as pd
import datetime

st.set_page_config(page_title="시가총액 Top 10 트렌드", layout="wide")

st.title("전 세계 시가총액 Top 10 기업 (최근 3년 변화)")

# 예시 데이터 생성 (실제 데이터로 교체 필요)
# 실제로는 Yahoo Finance API, Alpha Vantage, 또는 수동 수집된 CSV 사용 가능
companies = ['Apple', 'Microsoft', 'Saudi Aramco', 'Alphabet', 'Amazon',
             'Nvidia', 'Meta', 'Berkshire Hathaway', 'TSMC', 'Tesla']

dates = pd.date_range(end=datetime.datetime.today(), periods=36, freq='M')

data = {}
for company in companies:
    data[company] = (1000 + 500 * pd.Series(range(36))).apply(lambda x: x * (1 + 0.1 * (0.5 - pd.np.random.rand())))

df = pd.DataFrame(data, index=dates)

# 인터랙티브 Plotly 그래프
fig = go.Figure()

for company in df.columns:
    fig.add_trace(go.Scatter(x=df.index, y=df[company],
                             mode='lines+markers',
                             name=company))

fig.update_layout(
    title="Top 10 시가총액 기업의 3년간 변화",
    xaxis_title="날짜",
    yaxis_title="시가총액 (억 USD 가정)",
    hovermode='x unified',
    template='plotly_dark',
    height=600
)

st.plotly_chart(fig, use_container_width=True)
