import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date, datetime
import os

st.set_page_config(page_title="학습 & 운동 루틴 트래커", layout="wide")
st.title("📚💪 학습 & 운동 루틴 통합 트래커")

# 파일 경로 설정
LEARN_FILE = "learning_log.csv"
WORKOUT_FILE = "workout_log.csv"


# CSV 파일이 없으면 생성
def init_csv(file_path, columns):
    if not os.path.exists(file_path):
        pd.DataFrame(columns=columns).to_csv(file_path, index=False)


init_csv(LEARN_FILE, ["날짜", "카테고리", "학습 내용", "시간(분)", "메모"])
init_csv(WORKOUT_FILE, ["날짜", "운동 부위", "시간(분)", "메모"])

# 학습 기록 섹션
st.header("📘 학습 루틴 기록")
with st.form("study_form"):
    learn_date = st.date_input("날짜", date.today())
    learn_category = st.selectbox("카테고리", ["이론", "실습", "복습", "요약"])
    learn_topic = st.text_input("학습 내용")
    learn_duration = st.slider("학습 시간 (분)", 10, 180, 30)
    learn_memo = st.text_area("메모")
    learn_submit = st.form_submit_button("기록 저장")

if learn_submit:
    new_log = pd.DataFrame(
        [[learn_date, learn_category, learn_topic, learn_duration, learn_memo]],
        columns=["날짜", "카테고리", "학습 내용", "시간(분)", "메모"],
    )
    new_log.to_csv(LEARN_FILE, mode="a", header=False, index=False)
    st.success("학습 기록이 저장되었습니다.")

# 운동 기록 섹션
st.header("🏋️ 운동 루틴 기록")
with st.form("workout_form"):
    workout_date = st.date_input("운동 날짜", date.today())
    workout_part = st.selectbox("운동 부위", ["어깨", "가슴", "삼두", "이두", "등"])
    workout_duration = st.slider("운동 시간 (분)", 10, 90, 30)
    workout_memo = st.text_area("운동 메모")
    workout_submit = st.form_submit_button("운동 기록 저장")

if workout_submit:
    new_log = pd.DataFrame(
        [[workout_date, workout_part, workout_duration, workout_memo]],
        columns=["날짜", "운동 부위", "시간(분)", "메모"],
    )
    new_log.to_csv(WORKOUT_FILE, mode="a", header=False, index=False)
    st.success("운동 기록이 저장되었습니다.")

# 시각화 섹션
st.header("📊 주간 통계 시각화")
col1, col2 = st.columns(2)

# 학습 통계
with col1:
    st.subheader("학습 시간 통계")
    df_learn = pd.read_csv(LEARN_FILE)
    if not df_learn.empty:
        df_learn["날짜"] = pd.to_datetime(df_learn["날짜"])
        weekly_learn = df_learn.groupby(df_learn["날짜"].dt.strftime("%Y-%W"))[
            "시간(분)"
        ].sum()
        st.bar_chart(weekly_learn)
    else:
        st.info("학습 기록이 아직 없습니다.")

# 운동 통계
with col2:
    st.subheader("운동 시간 통계")
    df_workout = pd.read_csv(WORKOUT_FILE)
    if not df_workout.empty:
        df_workout["날짜"] = pd.to_datetime(df_workout["날짜"])
        weekly_workout = df_workout.groupby(df_workout["날짜"].dt.strftime("%Y-%W"))[
            "시간(분)"
        ].sum()
        st.bar_chart(weekly_workout)
    else:
        st.info("운동 기록이 아직 없습니다.")
