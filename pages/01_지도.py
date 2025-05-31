import streamlit as st
import folium
from streamlit_folium import st_folium

# 예술가들이 선호하는 여행지 데이터 (예시)
travel_destinations = [
    {"name": "파리, 프랑스", "lat": 48.8566, "lon": 2.3522, "desc": "모네와 피카소가 사랑한 도시, 세계적인 미술관의 중심지입니다."},
    {"name": "피렌체, 이탈리아", "lat": 43.7696, "lon": 11.2558, "desc": "르네상스의 발상지, 미켈란젤로와 다빈치의 흔적이 가득합니다."},
    {"name": "뉴욕, 미국", "lat": 40.7128, "lon": -74.0060, "desc": "현대 미술의 중심지, MoMA와 갤러리들이 즐비합니다."},
    {"name": "베를린, 독일", "lat": 52.5200, "lon": 13.4050, "desc": "예술과 자유정신이 공존하는 현대 예술의 메카입니다."},
    {"name": "도쿄, 일본", "lat": 35.6895, "lon": 139.6917, "desc": "전통과 현대 예술이 공존하는 아시아의 예술 허브입니다."},
    {"name": "바르셀로나, 스페인", "lat": 41.3851, "lon": 2.1734, "desc": "가우디의 도시, 건축 예술과 색채의 향연입니다."},
    {"name": "멕시코시티, 멕시코", "lat": 19.4326, "lon": -99.1332, "desc": "프리다 칼로와 디에고 리베라가 활동했던 예술의 도시입니다."},
    {"name": "상파울루, 브라질", "lat": -23.5505, "lon": -46.6333, "desc": "남미 현대 예술의 중심지입니다."},
    {"name": "마라케시, 모로코", "lat": 31.6295, "lon": -7.9811, "desc": "색감과 무늬, 수공예 예술의 영감을 주는 도시입니다."},
    {"name": "산프란시스코, 미국", "lat": 37.7749, "lon": -122.4194, "desc": "자유로운 창작 정신의 도시, 예술 공동체의 중심입니다."}
]

# Streamlit UI
st.title("🎨 예술가들이 사랑한 Top 10 여행지")
st.write("세계의 예술가들이 선호하는 도시를 지도와 함께 소개합니다.")

# 중심 좌표는 대략 중간 위치
m = folium.Map(location=[20, 0], zoom_start=2)

# 마커 추가
for place in travel_destinations:
    folium.Marker(
        location=[place["lat"], place["lon"]],
        popup=f"<b>{place['name']}</b><br>{place['desc']}",
        tooltip=place["name"],
        icon=folium.Icon(color='blue', icon='info-sign')
    ).add_to(m)

# Folium 맵 렌더링
st_data = st_folium(m, width=700, height=500)
