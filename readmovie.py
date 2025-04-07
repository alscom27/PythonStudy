with open("movies.csv", "r") as file:
    for line in file.readlines():
        data = line.split(",")
        (title, genre, year) = data
        print(f"{title:^10} | {genre:^10} | {year:^10}")

###
# 다음과 같은 , 구분된 한 반의 학생의 국어, 영어, 수학
# 점수가 목록으로 있다.
# 이 파일을 score.csv 파일로 저장하고 읽어서
# 이 반 학생 전체의 국어, 영어, 수학 과목별 평균 점수를
# 아래와 같이 출력하세요.

# [아래]
# 국어 평균 : xx.xx 점, 영어 평균 : xx.xx 점, 수학 평균 : xx.xx 점
# 번호, 이름 국어점수, 영어점수, 수학점수
# 1, 김영희, 100, 80, 65
# 2, 박영수, 85, 75, 70
# 3. 박나래 ,83, 73, 85
# 4. 박정희 ,67, 85, 90

# 파일 생성
# f = open("score.csv", "w", encoding="UTF=8")
# f.write("1,김영희,100,80,65\n")
# f.write("2,박영수,85,75,70\n")
# f.write("3,박나래,83,73,85\n")
# f.write("4,박정희,67,85,90\n")
# f.close()
sum = 0
avg = 0
with open("score.csv", "r", encoding="UTF-8") as file:
    korean = list()
    english = list()
    math = list()
    for line in file.readlines():
        (num, name, k, e, m) = line.split(",")
        korean.append(k)
        english.append(e)
        math.append(m)

    sum_k = 0
    sum_e = 0
    sum_m = 0
    for k in korean:
        sum_k += int(k)
    for e in english:
        sum_e += int(e)
    for m in math:
        sum_m += int(m)

    print(
        f"국어 평균 : {sum_k/4:8.2f}, 영어 평균 : {sum_e/4:8.2f}, 수학 평균 : {sum_m/4:8.2f}"
    )
