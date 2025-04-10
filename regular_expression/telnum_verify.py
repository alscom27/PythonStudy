import re

telnum = True
tel_exp = "0[1-8][0-9]?-[0-9]{3,4}-[0-9]{4}"

while telnum:
    try:
        telnum = input("[전화번호]>> ")
        if not telnum:
            raise Exception
        result = re.match(tel_exp, telnum)
    except:
        print("*입력오류* 전화번호가 제대로 입력되지 않았습니다.")
    else:
        if result:
            print("**성공** 전화번호가 제대로 입력되었습니다.")
        else:
            print("*번호오류* 전화번호가 형식에 맞지 않습니다.")
