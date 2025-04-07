import streamlit as st
import pandas as pd
from datetime import datetime, date
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode
import time

# 페이지 기본 설정
st.set_page_config(page_title="Todo List", layout="wide")

# 세션 상태 초기화
if "task_list" not in st.session_state:
    st.session_state.task_list = []
if "mode" not in st.session_state:
    st.session_state.mode = None
if "edit_index" not in st.session_state:
    st.session_state.edit_index = None

# 앱 제목
st.title("Todo-List")

# --------------------
# 할 일 목록 테이블 영역 (AgGrid 사용)
# --------------------
selected_index = None
if st.session_state.task_list:
    df = pd.DataFrame(st.session_state.task_list)

    gb = GridOptionsBuilder.from_dataframe(df)
    gb.configure_selection(selection_mode="single", use_checkbox=True)
    gb.configure_column("번호", width=80)
    grid_options = gb.build()

    grid_response = AgGrid(
        df,
        grid_options,
        height=400,
        update_mode=GridUpdateMode.SELECTION_CHANGED,
        fit_columns_on_grid_load=True,
    )

    selected = grid_response.get("selected_rows", [])
    if isinstance(selected, list) and len(selected) > 0:
        row = selected[0]
        if isinstance(row, dict) and "번호" in row:
            selected_index = int(row["번호"] - 1)
            st.session_state.edit_index = selected_index
else:
    st.info("할 일이 없습니다. 등록해주세요.")

# --------------------
# 상단 버튼 영역 (등록/수정/삭제/상태 변경)
# --------------------
col1, col2, col3, col4, col5 = st.columns([2, 2, 2, 2, 2])

with col1:
    if st.button(":heavy_plus_sign: 등록하기"):
        st.session_state.mode = "add"
        st.session_state.edit_index = None

with col2:
    if st.button(":pencil: 수정하기"):
        if st.session_state.edit_index is not None:
            st.session_state.mode = "edit"
        else:
            st.warning("수정할 항목을 선택하세요.")

with col3:
    if st.button(":x: 선택 항목 삭제"):
        if st.session_state.edit_index is not None:
            st.session_state.task_list.pop(st.session_state.edit_index)
            for i, task in enumerate(st.session_state.task_list):
                task["번호"] = i + 1
            st.success("삭제되었습니다.")
            st.session_state.edit_index = None
            st.rerun()
        else:
            st.warning("삭제할 항목을 선택하세요.")

with col4:
    if st.button(":white_check_mark: 상태 변경"):
        if st.session_state.edit_index is not None:
            current = st.session_state.task_list[st.session_state.edit_index]["상태"]
            st.session_state.task_list[st.session_state.edit_index]["상태"] = (
                "완료" if current == "진행 중" else "진행 중"
            )
            st.success("상태가 변경되었습니다.")
            st.rerun()
        else:
            st.warning("상태를 변경할 항목을 선택하세요.")

# --------------------
# 할 일 입력 폼 (등록 또는 수정) - 테이블보다 위에 출력
# --------------------
if st.session_state.mode in ["add", "edit"]:
    st.subheader("할 일 입력")

    default_task = ""
    default_date = date.today()

    if st.session_state.mode == "edit" and st.session_state.edit_index is not None:
        current_task = st.session_state.task_list[st.session_state.edit_index]
        default_task = current_task["할 일"]
        default_date = datetime.strptime(current_task["만료 기간"], "%Y-%m-%d").date()

    task = st.text_input("할 일을 입력하세요", value=default_task)
    due = st.date_input("기한을 입력하세요", value=default_date)

    c1, c2 = st.columns([1, 1])
    with c1:
        if st.button("확인"):
            if task:
                now = datetime.now().strftime("%Y-%m-%d")
                if st.session_state.mode == "add":
                    next_number = len(st.session_state.task_list) + 1
                    st.session_state.task_list.append(
                        {
                            "번호": next_number,
                            "할 일": task,
                            "상태": "진행 중",
                            "등록 기간": now,
                            "만료 기간": due.strftime("%Y-%m-%d"),
                        }
                    )
                elif (
                    st.session_state.mode == "edit"
                    and st.session_state.edit_index is not None
                ):
                    st.session_state.task_list[st.session_state.edit_index][
                        "할 일"
                    ] = task
                    st.session_state.task_list[st.session_state.edit_index][
                        "만료 기간"
                    ] = due.strftime("%Y-%m-%d")
                st.session_state.mode = None
                st.session_state.edit_index = None
                st.rerun()
            else:
                st.warning("할 일을 입력하세요.")

    with c2:
        if st.button("취소"):
            st.session_state.mode = None
            st.session_state.edit_index = None
            st.rerun()
