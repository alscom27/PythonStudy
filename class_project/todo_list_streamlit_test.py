# streamlit으로 만든 todo list
# streamlit : 파이썬 개발자들이 데이터 시각화, 대시보드, 웹앱을 엄청 쉽게 만들 수 있게 해주는 툴
# 파이썬으로 GUI 웹앱을 쉽게 만드는 프레임워크

# pip install streamlit
# 실행은 터미널에서 streamlit run 파일.py 명령어
# 디렉토리에 파일이 있어야함.
import streamlit as st
import pandas as pd
import time
from datetime import datetime

# pip install streamlit-aggrid
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode

head_col1, head_col2 = st.columns([8, 2])
with head_col1:
    st.title("Todo_List")

with head_col2:
    if st.button("화면 갱신"):
        st.rerun()


col1, col2, col3, col4, col5 = st.columns([2, 2, 2, 2, 2])

with col1:
    # st.write("메뉴")
    st.markdown("### 메뉴")

if "show_input" not in st.session_state:
    st.session_state.show_input = False

with col2:
    if st.button("등록하기"):
        st.session_state.show_input = True
        st.session_state.show_input_date = True
        st.session_state.update_input = False


if "task_list" not in st.session_state:
    st.session_state.task_list = []
    st.session_state.date_list = []


if st.session_state.show_input:
    new_task = st.text_input("할 일을 입력하세요.", key="new_task_input")
    complete_date = st.date_input("기한을 입력하세요.", key="complete_date_input")

    col1, col2, col3, col4 = st.columns([6, 2, 1, 1])
    with col3:
        if st.button("확인"):
            if new_task:
                if complete_date:
                    now_date = format(datetime.now(), ("%Y-%m-%d"))
                    done_date = format(complete_date, ("%Y-%m-%d"))
                    with col1:
                        st.success(f"'{new_task}'추가 완료")
                    st.session_state.task_list.append(
                        {
                            "할 일": new_task,
                            "상태": "진행 중",
                            "등록 기간": now_date,
                            "만료 기간": done_date,
                        }
                    )
                    st.session_state.show_input = False
                    time.sleep(0.5)
                    st.rerun()
            else:
                with col1:
                    st.warning("내용을 입력해주세요.")

    with col4:
        if st.button("취소"):
            st.session_state.show_input = False
            st.rerun()

if st.session_state.task_list:
    st.subheader("할 일 목록")

# col1, col2 = st.columns([3, 2])


# with col1:
# 테이블에 버튼 넣기 불가
if st.session_state.task_list:
    df = pd.DataFrame(st.session_state.task_list)
    # df.index = df.index + 1
    df.insert(0, "번호", range(1, len(df) + 1))

    gb = GridOptionsBuilder.from_dataframe(df)
    gb.configure_selection(selection_mode="multiple", use_checkbox=True)

    # 702
    gb.configure_column("번호", width=100)
    gb.configure_column("할 일", width=400)
    gb.configure_column("상태", width=120)
    gb.configure_column("등록 기간", width=250)
    gb.configure_column("만료 기간", width=250)

    grid_options = gb.build()

    grid_response = AgGrid(
        df,
        grid_options,
        fit_columns_on_grid_load=True,
        update_mode=GridUpdateMode.SELECTION_CHANGED,
    )

    selected_rows = grid_response["selected_rows"]

if "update_input" not in st.session_state:
    st.session_state.update_input = False

if not st.session_state.show_input:
    with col3:
        if st.button("수정하기"):
            st.session_state.show_input = False
            st.session_state.update_input = True
            st.session_state.update_date = True

if st.session_state.update_input:
    update_task_idx = (
        st.number_input(
            "수정할 일의 번호를 입력하세요.",
            min_value=1,
            step=1,
            format="%d",
            key="update_task_num_input",
        )
        - 1
    )
    update_task = st.text_input("수정할 일을 입력하세요.", key="update_task_input")
    update_date = st.date_input("수정할 기한을 입력하세요.", key="update_date_input")

    col1, col2, col3, col4 = st.columns([6, 2, 1, 1])
    with col3:
        if st.button("확인"):
            if 0 <= update_task_idx < len(st.session_state.task_list):
                if update_task:
                    if update_date:
                        with col1:
                            st.success(
                                f"""{st.session_state.task_list[update_task_idx]["할 일"]}가 {update_task}로 변경되었습니다.
만료 기간은 {st.session_state.task_list[update_task_idx]["만료 기간"]}에서 {format(update_date, "%Y-%m-%d")}로 변경되었습니다."""
                            )

                            st.session_state.task_list[update_task_idx][
                                "할 일"
                            ] = update_task
                            st.session_state.task_list[update_task_idx]["만료 기간"] = (
                                format(update_date, "%Y-%m-%d")
                            )
                            st.session_state.update_input = False
                            time.sleep(1)
                            st.rerun()
                else:
                    with col1:
                        st.warning("수정할 내용을 압력해주세요.")
            elif 0 <= update_task_idx >= len(st.session_state.task_list):
                with col1:
                    st.warning("변경하려는 항목이 없습니다.")
    with col4:
        if st.button("취소"):
            st.session_state.update_input = False
            st.rerun()


if not st.session_state.show_input:
    # and not st.session_state.update_input
    with col4:
        if st.button("삭제하기"):
            if selected_rows is not None and len(selected_rows) > 0:
                selected_indices = []
                for row in selected_rows:
                    if isinstance(row, dict) and "번호" in row:
                        selected_indices.append(int(row["번호"]) - 1)

                # selected_indices = [int(row["번호"]) - 1 for row in selected_rows]
                for idx in sorted(selected_indices, reverse=True):
                    st.session_state.task_list.pop(idx)

                grid_response["selected_rows"].clear()

                with col1:
                    st.success("선택한 항목이 삭제되었습니다.")
                    time.sleep(0.5)
                    st.rerun()
            else:
                with col1:
                    st.warning("삭제할 항목이 없습니다.")
                    time.sleep(0.5)
                    st.rerun()

with col5:
    st.button("상태 변경")
