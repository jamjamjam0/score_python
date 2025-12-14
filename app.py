import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_title="큐트 성적 계산기",
    page_icon="🎀",
    layout="centered"
)

# 1. 제목과 설명
st.title("💖 큐트 성적 계산기 💖")
st.write("이번 학기 점수를 입력하면 학점을 알려드려요! 🐰")

# 2. 점수 입력 받기
score = st.number_input("점수를 입력해 주세요 (0~100)", min_value=0, max_value=100, step=1)

# 3. 버튼 클릭 시 로직 실행
if st.button("결과 확인하기 ✨"):
    grade = ''
    message = ''
    color = ''

    if score >= 90:
        grade = 'A'
        message = "와우! 정말 대단해요! 🎉"
        color = "blue"
        st.balloons()
    elif score >= 80:
        grade = 'B'
        message = "참 잘했어요! 👏"
        color = "green"
    elif score >= 70:
        grade = 'C'
        message = "조금만 더 힘내요! 💪"
        color = "orange"
    elif score >= 60:
        grade = 'D'
        message = "포기하지 마세요! ✨"
        color = "brown"
    else:
        grade = 'F'
        message = "다음엔 더 잘할 수 있어요! 🍀"
        color = "red"
        
    # 결과 보여주기
    st.markdown(f"### 당신의 학점은 :{color}[{grade}] 입니다.")
    st.info(message)
