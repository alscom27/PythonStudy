#  콘솔로 todo_list 만들어보기
# 1. 할 일 목록
# 2. 할 일 추가
# 3. 할 일 삭제
# 4. 종료

# +사용자 추가 삭제

import time


# 로딩표시
def loading():
    for num in range(3):
        print(".", end="", flush=True)
        time.sleep(0.5)


# print("Todo-List")


# todo-list 실행 함수
def todo():
    # 구분자
    line = "=" * 10

    # 메인 메뉴
    main_menu = f"""
{line-3} main {line-3}
1. 할 일 목록 불러오기
2. 할 일 추가하기
3. 할 일 삭제하기
4. 종료
{line*2}
"""
    # 목록
    todo_list = []

    while True:
        print(f"Todo-List 시작하시겠습니까?/n1. 예/n2. 아니오")

        try:
            click = int(input("메뉴 번호를 입력해주세요./n"))

            if click == 1:
                print("사용자 이름을 입력해주세요.")
            user_name = input("사용자 이름 : ")
            print(f"{user_name}님의 Todo-List")

            while True:
                print(main_menu)
                click = int(input("메뉴 번호를 눌러주세요."))

                if click == 1:
                    for i in range(len(todo_list)):
                        print(f"{i+1}. {todo_list[i]}/n")
                        print(line * 2)

                # elif click == 2 :

                # elif click == 3 :

                # elif click == 4 :

                # else :
                #     break

            # elif click == 2 :
            #     print("Todo-List를 종료합니다.")
            #     loading()
            #     break

        except ValueError:
            print("잘못된 입력입니다.")
            loading()
            print("처음으로 돌아갑니다.")
            todo()
