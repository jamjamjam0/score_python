import tkinter as tk
from tkinter import messagebox

def calculate_grade():
    try:
        # 입력창(entry)에서 내용을 가져와 숫자로 변환
        score_text = entry.get()
        score = int(score_text)
        
        # 성적 처리 로직
        if score >= 90:
            grade = 'A'
            message = "와우! 정말 대단해요! 🎉"
        elif score >= 80:
            grade = 'B'
            message = "참 잘했어요! 👏"
        elif score >= 70:
            grade = 'C'
            message = "조금만 더 힘내요! 💪"
        elif score >= 60:
            grade = 'D'
            message = "포기하지 마세요! ✨"
        else:
            grade = 'F'
            message = "다음엔 더 잘할 수 있어요! 🍀"
            
        # 결과 라벨 업데이트
        result_label.config(text=f"당신의 학점은 '{grade}' 입니다.\n{message}", fg="#FF69B4")
        
    except ValueError:
        # 숫자가 아닌 것을 입력했을 때 경고창
        messagebox.showwarning("입력 오류", "숫자로 된 점수만 입력해주세요! 🥺")

# 1. 윈도우 설정 (기본 틀)
window = tk.Tk()
window.title("💖 큐트 성적 계산기 💖")
window.geometry("350x400")
window.configure(bg="#FFF0F5") # 배경색: 라벤더 블러쉬 (연한 분홍)

# 2. 제목 라벨
title_label = tk.Label(window, text="성적을 입력해 주세요 🎀", 
                       font=("맑은 고딕", 16, "bold"), 
                       bg="#FFF0F5", fg="#FF69B4")
title_label.pack(pady=40) # 위아래 여백

# 3. 점수 입력창
entry = tk.Entry(window, font=("맑은 고딕", 14), width=15, justify="center",
                 bd=2, relief="solid")
entry.pack(pady=10)

# 4. 확인 버튼 (꾸미기)
btn = tk.Button(window, text="결과 확인하기 🐰", 
                font=("맑은 고딕", 12, "bold"),
                bg="#FFB6C1", fg="white", # 배경: 연분홍, 글자: 흰색
                activebackground="#FF69B4", # 클릭했을 때 색상
                width=20, height=2,
                relief="flat", # 테두리 없애기
                command=calculate_grade) # 버튼 누르면 함수 실행
btn.pack(pady=20)

# 5. 결과 보여주는 곳
result_label = tk.Label(window, text="", 
                        font=("맑은 고딕", 14, "bold"), 
                        bg="#FFF0F5", fg="#555555")
result_label.pack(pady=20)

# 6. 프로그램 실행 (무한 루프)
window.mainloop()
