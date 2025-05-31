import streamlit as st

st.set_page_config(page_title="퍼스널 컬러 화장품 추천기", layout="centered")

st.title("💄 퍼스널 컬러 기반 화장품 추천기")

# Step 1: 퍼스널 컬러 선택
st.subheader("1. 퍼스널 컬러를 선택하세요")
personal_color = st.selectbox(
    "당신의 퍼스널 컬러는 무엇인가요?",
    ["봄웜", "여름쿨", "가을웜", "겨울쿨"]
)

# Step 2: 화장품 종류 선택
st.subheader("2. 화장품 종류를 선택하세요")
cosmetic_type = st.selectbox(
    "어떤 종류의 화장품을 찾고 계신가요?",
    ["립", "파운데이션", "아이섀도우", "블러셔", "마스카라"]
)

# 추천 결과 딕셔너리
recommendations = {
    "봄웜": {
        "립": ("3CE 립 컬러", "https://www.stylenanda.com/category/3ce-lip/2001/"),
        "파운데이션": ("에스쁘아 비 실크 파운데이션", "https://www.espoir.com/ko/pd/100112006"),
        "아이섀도우": ("클리오 프로 아이 팔레트 코랄", "https://www.cliocosmetic.com/ko/product/detail?productId=123"),
        "블러셔": ("페리페라 잉크 블러셔", "https://www.peripera.co.kr/ko/blush"),
        "마스카라": ("이니스프리 스키니 마스카라", "https://www.innisfree.com/kr/ko/product/productView.do?prdSeq=26161")
    },
    "여름쿨": {
        "립": ("롬앤 쥬시 래스팅 틴트 쿨톤 컬러", "https://romand.co.kr/product/list.html?cate_no=68"),
        "파운데이션": ("라네즈 네오 쿠션", "https://www.laneige.com/kr/ko/product/makeup/neo-cushion-matte.html"),
        "아이섀도우": ("에뛰드 플레이 컬러 아이즈 라벤더", "https://www.etude.com/kr/ko/product/553002343"),
        "블러셔": ("투쿨포스쿨 아트클래스 바이로댕 블러셔", "https://www.toocoolforschool.com/product/list.html?cate_no=46"),
        "마스카라": ("클리오 킬래쉬 마스카라", "https://www.cliocosmetic.com/ko/product/detail?productId=209")
    },
    "가을웜": {
        "립": ("맥 칠리 립스틱", "https://www.maccosmetics.co.kr/product/13854/310/products/makeup/lips/lipstick/lipstick"),
        "파운데이션": ("헤라 글로우 래스팅 파운데이션", "https://www.hera.com/kr/ko/product/glow-lasting-foundation.html"),
        "아이섀도우": ("루나 아이팔레트 오렌지 브라운", "https://www.luna.co.kr/product/detail?productId=101"),
        "블러셔": ("나스 오르가즘 블러셔", "https://www.narscosmetics.kr/ko/blush/0607845015013.html"),
        "마스카라": ("키스미 히로인 마스카라 브라운", "https://www.kissme.co.kr/product/detail?productId=201")
    },
    "겨울쿨": {
        "립": ("디올 루즈 디올 포에버", "https://www.dior.com/ko_kr/products/beauty-Y0996419-%EB%A3%A8%EC%A5%AC-%EB%94%94%EC%98%AC-%ED%8F%AC%EC%97%90%EB%B2%84-%EB%A7%A4%ED%8B%B0%ED%94%84%EB%A0%88%EC%83%89-%EB%A6%BD%EC%8A%A4%ED%8B%B1"),
        "파운데이션": ("에스티로더 더블웨어", "https://www.esteelauder.co.kr/product/643/32264/product-catalog/makeup/face/foundation/double-wear-stay-in-place-makeup/spf-10"),
        "아이섀도우": ("어반디케이 네이키드3 쿨톤", "https://www.urbandecay.co.kr/product/detail.jsp?prod_id=UR20362"),
        "블러셔": ("입생로랑 꾸뛰르 블러쉬", "https://www.yslbeautykr.com/ko_KR/makeup/face/blush/"),
        "마스카라": ("베네피트 롤러 래쉬", "https://www.benefitcosmetics.com/kr/ko/product/roller-lash")
    }
}

# 결과 출력
st.subheader("3. 추천 제품 보기")

if personal_color and cosmetic_type:
    product_name, product_url = recommendations[personal_color][cosmetic_type]
    st.markdown(f"🎯 **추천 제품:** [{product_name}]({product_url})")
    st.markdown(f"🔗 [제품 보러가기]({product_url})")

