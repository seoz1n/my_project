import streamlit as st
import yfinance as yf
import plotly.graph_objs as go
import pandas as pd
import datetime

st.set_page_config(page_title="Top 10 시가총액 기업 추세", layout="wide")
st.title("전 세계 시가총액 Top 10 기업 주가 변화 (최근 3년)")

# 티커 목록과 매핑
tickers = {
    'Apple': 'AAPL',
    'Microsoft': 'MSFT',
    'Saudi Aramco': '2222.SR',
    'Alphabet (Google)': 'GOOG',
    'Amazon': 'AMZN',
    'Nvidia': 'NVDA',
    'Meta Platforms': 'META',
    'Berkshire Hathaway': 'BRK-B',
    'TSMC': 'TSM',
    'Tesla': 'TSLA'
}

start_date = (datetime.datetime.today() - pd.DateOffset(years=3)).strftime('%Y-%m-%d')
end_date = datetime.datetime.today().strftime('%Y-%m-%d')

@st.cache_data(show_spinner=True)
def load_data(tickers):
    df = pd.DataFrame()
    for name, ticker in tickers.items():
        try:
            stock = yf.Ticker(ticker)
            hist = stock.history(start=start_date, end=end_date, interval="1mo")
            df[name] = hist['Close']
        except Exception as e:
            st.warning(f"{name} 데이터 로드 실패: {e}")
    return df

with st.spinner("데이터 로딩 중..."):
    data = load_data(tickers)

# 그래프 그리기
fig = go.Figure()
for company in data.columns:
    fig.add_trace(go.Scatter(x=data.index, y=data[company],
                             mode='lines+markers', name=company))

fig.update_layout(
    title="Top 10 시가총액 기업의 월별 종가 변화 (최근 3년)",
    xaxis_title="날짜",
    yaxis_title="종가 (USD)",
    hovermode="x unified",
    template="plotly_dark",
    height=600
)

st.plotly_chart(fig, use_container_width=True)
