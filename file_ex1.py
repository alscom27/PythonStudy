# 파일 생성하기 현재 디렉토리에 파일 생성

# r : 읽기모드 ,w : 쓰기모드 , a : 추가모드
# 파일객체(경로, 파일열기모드)
# 쓰기모드의 경우 이미 파일에 내용이 있다면 지워지고 새로덮어짐.
# 저장하거나 읽을 때 인코딩 맞추기 EUC_KR과 UTF-8은 다름
# 나중에 배포할 시스템이 리눅스면 UTF-8 추천 윈도우면 EUC_KR 추천
# 그냥 UTF-8이 나은거같은데?
# f = open("새파일.txt", "a", encoding="UTF-8")
# f.write("\n나의 친구는 미국인 입니다.")
# f.close()

# 윈도우를 제외한 모든건 디렉토리 C:/doit /로 경로 표현
# 윈도우는 \ 역슬래시로 경로 표현
# cd \ :루트로 이동, mkdir :디렉토리에 폴더?생성
# f = open("C:/doit/새파일.txt", "w")
# f.close()

# f = open("새파일.txt", "w", encoding="UTF-8")
# for i in range(1, 11):
#     data = "%d번째 줄입니다.\n" % i
#     f.write(data)
# f.close()


# readline() : 한 라인씩 읽어옴.
# f = open("새파일.txt", "r", encoding="UTF-8")
# line = f.readline()
# print(line)  # 첫번재 줄
# line = f.readline()
# print(line)  # 두번째 줄
# f.close()

# f = open("새파일.txt", "r", encoding="UTF-8")
# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line)
# f.close()

# readlines() : 파일전체를 한줄씩 리스트로
# lines = f.readlines()
# for line in lines:
#     print(
#         line, end=""
#     )  # 입력할 때 개행문자를 하나 넣었기때문에 그냥 print하면 2줄 개행된것처럼 나옴
# f.close()

# read() : 파일전체를 읽음
# data = f.read()
# print(data)
# f.close()

############
# with문 : 파일오플하고 인덴트문 다 끝나면 자동으로 파일close해줌.

with open("새파일.txt", mode="r", encoding="UTF-8") as file:
    content = list()

    while True:
        sentence = file.readline()

        if sentence:
            content.append(sentence)
        else:
            break

    print(content)

with open("새파일.txt", "r", encoding="UTF-8") as file:
    content = list()
    for f in file:
        content.append(f)
    print(content)

print()

# a모드 append모드
# f = open("새파일.txt", "a", encoding="UTF-8")
# for i in range(11, 20):
#     data = "%d번재 줄입니다.\n" % i
#     f.write(data)
# f.close()

with open("새파일.txt", "w", encoding="UTF-8") as file:
    words = ["Python\n", "파이썬\n", "YOUNEED"]
    file.write("START\n")
    file.writelines(words)
    file.write("END")
    file.write("Hello")
