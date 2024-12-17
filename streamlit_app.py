import streamlit as st

# MBTI에 따른 직업 및 성격 분석
mbti_profiles = {
    "ISTJ": {
        "job": "회계사, 변호사, 공무원",
        "compatibility": "신뢰할 수 있고 체계적인 사람과 잘 맞아요! 🚶‍♂️📚"
    },
    "ISFJ": {
        "job": "간호사, 교사, 상담사",
        "compatibility": "친절하고 따뜻한 사람과 좋은 관계를 맺어요! 💖👩‍⚕️"
    },
    "INFJ": {
        "job": "작가, 심리학자, 상담사",
        "compatibility": "창의적이고 깊은 사고를 하는 사람과 잘 맞아요! 📝🧠"
    },
    "INTJ": {
        "job": "전략가, 연구원, CEO",
        "compatibility": "논리적이고 독립적인 사람과 잘 맞아요! 🔍🧑‍💻"
    },
    "ISTP": {
        "job": "기술자, 엔지니어, 운동선수",
        "compatibility": "실용적이고 모험적인 사람과 잘 맞아요! ⚙️🏎️"
    },
    "ISFP": {
        "job": "예술가, 디자이너, 음악가",
        "compatibility": "감성적이고 자유로운 사람과 잘 맞아요! 🎨🎶"
    },
    "INFP": {
        "job": "작가, 예술가, 사회 운동가",
        "compatibility": "이상적이고 감정이 풍부한 사람과 잘 맞아요! 🌱💭"
    },
    "INTP": {
        "job": "철학자, 과학자, 프로그래머",
        "compatibility": "호기심 많고 논리적인 사람과 잘 맞아요! 🧠💡"
    },
    "ESTP": {
        "job": "마케팅 전문가, 운동선수, 기업가",
        "compatibility": "활동적이고 에너지 넘치는 사람과 잘 맞아요! 💪🏃‍♂️"
    },
    "ESFP": {
        "job": "연예인, 이벤트 플래너, 사회복지사",
        "compatibility": "사교적이고 즐거운 사람과 잘 맞아요! 🎉🌟"
    },
    "ENFP": {
        "job": "광고 디자이너, 작가, 상담사",
        "compatibility": "창의적이고 유머러스한 사람과 잘 맞아요! 🎈🦄"
    },
    "ENTP": {
        "job": "발명가, 변호사, 컨설턴트",
        "compatibility": "도전적이고 논리적인 사람과 잘 맞아요! ⚡💡"
    },
    "ESTJ": {
        "job": "경영자, 관리자, 군인",
        "compatibility": "목표 지향적이고 책임감 있는 사람과 잘 맞아요! 🏅📊"
    },
    "ESFJ": {
        "job": "간호사, 교육자, 사회복지사",
        "compatibility": "배려심 많고 친근한 사람과 잘 맞아요! 🤝💐"
    },
    "ENFJ": {
        "job": "교사, 지도자, 카운슬러",
        "compatibility": "영감을 주고 서로를 이끌어가는 사람과 잘 맞아요! 🌟👫"
    },
    "ENTJ": {
        "job": "CEO, 기업가, 전략가",
        "compatibility": "리더십을 발휘할 수 있는 동료와 잘 맞아요! 🧑‍💼👑"
    }
}

# Streamlit 앱 제목
st.title("MBTI 직업 & 성격 분석 🔮")

# MBTI 선택 드롭다운 메뉴
mbti_choice = st.selectbox("나의 MBTI를 선택하세요!", list(mbti_profiles.keys()))

# 선택된 MBTI에 대한 직업과 성격 분석 표시
if mbti_choice:
    st.write(f"### {mbti_choice}의 적합한 직업 및 성격")
    st.write(f"🔹 직업: {mbti_profiles[mbti_choice]['job']}")
    st.write(f"🔹 성격 적합도: {mbti_profiles[mbti_choice]['compatibility']}")
