import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Streamlit 앱 타이틀
st.title("중학생 과학 시뮬레이션 📊")

# 교육과정 선택
course_option = st.selectbox(
    "어떤 과학 시뮬레이션을 체험하고 싶나요? 🤔",
    ["뉴턴의 운동 법칙", "물질의 상태 변화"]
)

if course_option == "뉴턴의 운동 법칙":
    st.subheader("뉴턴의 운동 법칙 시뮬레이션 🏃‍♂️💨")
    st.write("뉴턴의 제2법칙(F = ma)은 힘, 질량, 가속도의 관계를 설명합니다.")
    
    # 사용자 입력 받기
    mass = st.slider("물체의 질량을 선택하세요 (kg)", 1, 10, 5)
    acceleration = st.slider("물체의 가속도를 선택하세요 (m/s²)", 1, 10, 3)
    
    # 뉴턴의 제2법칙 계산
    force = mass * acceleration
    st.write(f"물체에 작용하는 힘은: {force} N (뉴턴)입니다.")
    
    # 그래프 그리기
    fig, ax = plt.subplots()
    ax.plot([0, 1], [0, force], label=f'힘 = {force} N', color="blue")
    ax.set_title("힘-가속도 관계 그래프")
    ax.set_xlabel("가속도 (m/s²)")
    ax.set_ylabel("힘 (N)")
    ax.legend()
    st.pyplot(fig)

elif course_option == "물질의 상태 변화":
    st.subheader("물질의 상태 변화 시뮬레이션 🔥❄️")
    st.write("온도에 따른 물질의 상태 변화를 알아봅니다. 물질은 고체, 액체, 기체로 변화할 수 있습니다.")
    
    # 사용자 입력 받기
    temperature = st.slider("온도를 선택하세요 (°C)", -50, 150, 20)
    
    if temperature <= 0:
        state = "고체 ❄️"
    elif temperature <= 100:
        state = "액체 💧"
    else:
        state = "기체 ☁️"
    
    st.write(f"선택한 온도 ({temperature}°C)에서 물질의 상태는: {state}입니다.")
    
    # 상태 변화 그래프
    fig, ax = plt.subplots()
    temperatures = np.linspace(-50, 150, 100)
    states = ["고체" if temp <= 0 else "액체" if temp <= 100 else "기체" for temp in temperatures]
    
    ax.plot(temperatures, states, color="green")
    ax.set_title("물질의 상태 변화 (온도에 따른 상태 변화)")
    ax.set_xlabel("온도 (°C)")
    ax.set_ylabel("물질의 상태")
    st.pyplot(fig)

st.write("이 시뮬레이션은 과학 개념을 이해하고, 실험을 통해 그 관계를 시각적으로 탐구할 수 있는 도구입니다. 즐기세요! 😊")
