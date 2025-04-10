days = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
date = True

while date:
    try:
        date = input("날짜 <월 일>을 입력하세요: ")
        mm, dd = date.split()
        mm, dd = int(mm), int(dd)
        if mm < 1 or mm > 12:
            raise ValueError("월은 1에서 12까지")
        if dd < 1 or dd > days[mm - 1]:
            raise ValueError(f"일은 1에서 {days[mm-1]}까지")
    except ValueError as e:
        print("[입력 오류]", e)
    else:
        print(f"{mm}월 {dd}일")
