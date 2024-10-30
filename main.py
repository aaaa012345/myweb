import streamlit as st

menu = st.sidebar.selectbox("MENU",["로그인", "회원가입"])

db_id = "test"
db_pw = "123"

if menu == "로그인":
    st.title("로그인")
    id = st.text_input("아이디", placeholder="아이디를 입력하세요.")
    pw = st.text_input("비밀번호", type="password")
    login = st.button("로그인")

    if db_id == id and db_pw == pw:
        st.success("로그인 성공")
        st.balloons()
    else:
        st.error("로그인 실패")
        st.snow()
elif menu == "회원가입":
    st.title("회원가입")
    st.video("https://www.youtube.com/watch?v=8dYNg7bmS5c")



# 과목 = st.selectbox("과목을 선택하세요",
#                     ["확률과 통계",
#                      "미분과 적분",
#                      "기하와 벡터"])
# st.subheader(f"당신이 선택한 과목은 {과목}입니다.")


# 짜장면 = st.checkbox("짜장면(5000원)")
# 짬뽕 = st.checkbox("짬뽕(7000원)")
# 탕수육 = st.checkbox("탕수육(12000원)")
# 가격 = 0
# if 짜장면:
#     가격 += 5000
# if 짬뽕:
#     가격 += 7000
# if 탕수육:
#     가격 += 12000

# st.subheader(f"선택한 음식의 가격은 {가격}입니다.")





# 버튼 = st.button("버튼")
# if 버튼:
#     st.write("버튼을 눌렀습니다.")




# st.title("😎Title")
# st.header("Header")
# st.subheader("Subheader")
# st.write("작은 글씨")
# st.markdown("우리 함께 **스트림릿**을 :red[배워]봅시다!!!")
# st.write("우리 함께 **스트림릿**을 :blue[배워]봅시다!!!")