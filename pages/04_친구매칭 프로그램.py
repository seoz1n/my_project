import streamlit as st
import folium
from streamlit_folium import st_folium
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderUnavailable

st.set_page_config(page_title="친구 매치 프로그램", layout="wide")

st.title("🎯 주변 또래 친구 매치 프로그램")

# 지오로케이터 초기화
geolocator = Nominatim(user_agent="friend_match_app")

st.subheader("🗺️ 지도에서 지역 선택")

# 기본 지도 위치
m = folium.Map(location=[37.5665, 126.9780], zoom_start=11)  # 서울 기준
map_data = st_folium(m, width=700, height=500)

selected_location = ""
if map_data and map_data["last_clicked"]:
    lat = map_data["last_clicked"]["lat"]
    lon = map_data["last_clicked"]["lng"]
    try:
        location_info = geolocator.reverse((lat, lon))
        if location_info:
            selected_location = location_info.address
            st.info(f"선택된 주소: {selected_location}")
    except GeocoderUnavailable:
        st.error("주소를 가져오는 데 실패했습니다. 나중에 다시 시도해주세요.")

# 사용자 정보 입력 폼
with st.form("user_info_form"):
    st.subheader("📋 내 정보 입력")
    col1, col2 = st.columns(2)
    
    with col1:
        name = st.text_input("이름")
        age = st.number_input("나이", min_value=10, max_value=100, step=1)
        gender = st.selectbox("성별", ["남자", "여자", "기타"])
        mbti = st.text_input("MBTI (예: INFP)")
    
    with col2:
        location = st.text_input("지역 (지도를 클릭하면 자동 입력)", value=selected_location)
        instagram = st.text_input("인스타그램 아이디", placeholder="@your_id")
        interests = st.text_area("관심 분야 (쉼표로 구분)", placeholder="음악, 운동, 게임 등")

    submitted = st.form_submit_button("친구 매칭 시작!")

# 폼 제출 시 처리
if submitted:
    if not instagram.strip():
        st.warning("⚠ 인스타그램 아이디는 필수입니다.")
    elif not interests.strip():
        st.warning("⚠ 관심 분야는 필수입니다.")
    else:
        st.success("입력 완료! 아래에서 정보를 확인하세요.")

        # 사용자 정보 출력
        with st.container():
            st.subheader("📇 내 친구 매칭 정보")
            st.markdown(f"""
            - **이름**: {name}  
            - **나이**: {age}  
            - **성별**: {gender}  
            - **MBTI**: {mbti}  
            - **지역**: {location}  
            - **인스타**: @{instagram}  
            - **관심 분야**: {interests}  
            """)

