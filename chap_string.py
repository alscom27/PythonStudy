str1 = 'Life is too short\nYou need python'
print(str1)

# 문자열 앞에 r = 행 그대로(문자 그대로를 출력하기 위해 사용)
str2 = r"\n"
print(str2)

str3 = "Life is too short, You need python"
print(str3)
print(str3[-1])
print(str3[-2])

print(len(str3))

# %d %s, %(10, 'str')
num1 = 10
print("가나다라%d마바사%s" %(num1, str1))

pi = 3.141592
print("파이는 %f 입니다." %pi)
print("파이는 %.2f 입니다." %pi)
print("파이는 %0.2f 입니다." %pi)
print("파이는 {}입니다.".format(pi))
print("파이는 {:.2f}입니다.".format(pi))

# 문자열 앞에 f = 포매팅
msg = f"이 숫자는 {num1} 입니다."
print(msg)

print(f"파이는 {pi:5.2f} 입니다.")

str4 = str3.replace("Life", "Your leg")
print(str4)

str5 = "영어, 국어, 수학, 과학"
list = str5.split(', ')
print(list)

print("="*50)

rrn = "881120-1068324"
print("홍길동의 주민번호는 {} 입니다.".format(rrn[:6] + '-' + rrn[7:]))

birth_date = rrn[:6]
post_date = rrn[7:]
print("홍길동의 birth_date:{}, post_date:{}입니다.".format(birth_date, post_date))

print("="*50)

pin = "881120-1068234"

if(int(pin[7]) == 1) :
    print("남자입니다.")
else :
    print("여자입니다.")

print("남자입니다." if(int(pin[7]) == 1) else "여자입니다.")

print("="*50)

str_a = "a:b:c:d"
print(str_a.replace(":", "#"))
str_b = "abad"
print(str_b.replace(str_b[2], "c")) # 두번째 a만 안되네

## practice
# 예) http://naver.com
# 규칙1 : http:// 부분은 제외 => naver.com
# 규칙 2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙 3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성
#               (nav)               (5)         (1)             (!)
# 예) 생성된 비밀번호 : nav51!

url = "http://naver.com"
rule1 = url[url.rfind("/")+1:]
# rule1 = url.replace("http://", "")
print(rule1)

rule2 = rule1[:rule1.find(".")]
print(rule2)

r3_pass = rule2[:3] + str(len(rule2)) + str(rule2.count("e")) + "!"
print("{}에 생성된 비밀번호는 {}입니다.".format(url, r3_pass))