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

    print()


# print("Todo-List")


# todo-list 실행 함수
def todo():
    # 구분자
    line = "=" * 10

    # 메인 메뉴
    main_menu = f"""{line[:len(line)-3]} main {line[:len(line)-3]}
1. 할 일 목록 불러오기
2. 할 일 추가하기
3. 할 일 삭제하기
4. 시작 메뉴로 돌아가기
{line*2}"""
    # 목록

    while True:
        todo_list = []

        try:

            print(
                """Todo-List 시작하시겠습니까?
1. 시작
2. 종료"""
            )
            click = int(input("메뉴 번호를 입력해주세요. "))

            if click == 1:
                print("사용자 이름을 입력해주세요. ")
                user_name = input("사용자 이름 : ")
                print()
                print(
                    f"{user_name}님의 Todo-List📝",
                )

                while True:
                    print(main_menu)
                    click = int(input("메뉴 번호를 눌러주세요. "))

                    if click == 1:
                        print(f"목록 불러오는중", end="")
                        loading()

                        if len(todo_list) > 0:
                            print(line * 2)
                            print(f"{user_name}님의 Todo-List📝")
                            for i in range(len(todo_list)):
                                print(f"{i+1}. {todo_list[i]}")
                            print(line * 2)
                            continue

                        else:
                            print(f"{user_name}님의 Todo-List📝")
                            print("비어있는 목록")
                            print(line * 2)
                            continue

                    elif click == 2:
                        reg_todo = input("할 일을 입력해주세요. ")

                        if reg_todo.isdigit():
                            # isdigit : 문자열이 숫자로만 구성되어있는지 확인
                            loading()
                            print("⚠️숫자만 입력할 수 없습니다.\nmain으로 돌아갑니다.")
                            continue

                        else:
                            print(f'"{reg_todo}"등록 중', end="")
                            loading()

                            todo_list.append(reg_todo)

                            print("✔️등록되었습니다.")
                            print(line * 2)
                            continue

                    elif click == 3:
                        print(f"목록 불러오는중", end="")
                        loading()

                        if len(todo_list) > 0:
                            print(line * 2)
                            print(f"{user_name}님의 Todo-List📝")
                            for i in range(len(todo_list)):
                                print(f"{i+1}. {todo_list[i]}")
                            print(line * 2)

                            del_num = int(
                                input("🗑️삭제 할 항목의 번호를 입력해주세요. ")
                            )
                            print(line * 2)

                            del_todo = todo_list.pop(del_num - 1)
                            print(
                                f"""⚠️정말 {del_todo}을(를) 삭제하시겠습니까?
1. 예
2. 아니오"""
                            )

                            click = int(input("선택할 메뉴의 번호를 눌러주세요. "))
                            print(line * 2)

                            if click == 1:
                                print("삭제하는 중", end="")
                                loading()
                                print("✔️삭제가 완료되었습니다.")
                                continue

                            elif click == 2:
                                print("삭제를 취소했습니다.\nmain으로 돌아갑니다.")
                                todo_list.insert(del_num - 1, del_todo)
                                continue

                        else:
                            print(f"{user_name}님의 Todo-List📝")
                            print("비어있는 목록")
                            print(line * 2)
                            continue

                    elif click == 4:
                        print("시작 메뉴로 돌아갑니다.")
                        loading()
                        break

                    else:
                        print("⚠️잘 못 입력했습니다. 다시 눌러 주세요.")
                        continue

            elif click == 2:
                loading()
                print("Todo-List를 종료합니다.")
                break

        except ValueError:
            print("⚠️잘못된 입력입니다.")
            loading()
            print("처음으로 돌아갑니다.")
            continue


# todo 실행
todo()
