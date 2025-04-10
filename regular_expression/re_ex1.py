# 실제로 정규식이 꼭 필요한 경우
# 1. 주민번호 : 패턴이 정해져있는 경우
# 2. 비밀번호 패턴 : 8자리이상(10자리 이상) , 영문 대문자/소문자 1개 이상씩 포함, 특수문자 허용안함, 특수문자는 !@#$% 허용
# 3. 검색 할 때 Regular Expression 정규표현식을 써야하는데
# => 검색은 RE => DB에 의존하게 됨


import re


p = re.compile("[a-z]+")

# match() : 앞에서부터 읽기 시작
# m = p.match("python")
m = p.match("3 python")  # none
# match()는 앞에서부터 찾기 시작하기 때문에 앞에 3이 나와서 none을 반환한듯
print(m)

m2 = p.match("string goes here")
if m2:
    print("Match found :", m2.group())  # .group() 은 매치된 값을 반환해줌.
else:
    print("No match")

m = p.match("python")
print(m.start())  # 0
print(m.end())  # 6
print(m.span())  # (0, 6)

# search() : 전체를 읽어서 첫번째 나오는 값 반환 뒤에까지안감.
m = p.search("python")  # match는 앞에서부터여서 못찾았지만 search는 찾을수 있음
print(m)

m = p.search("3 python")
print(m)

# findall : 다 찾음
result = p.findall("life is too short")
print(result)

result = p.finditer("life is too short")
print(result)  # 이터레이터 형태?로반환
for rs in p.finditer("life is too short"):
    print(rs)

# . (dot)은 어떤문자던지 한개를 모두허용 이라는 뜻인데 안되는게 개행문자 이건 안됨.
p = re.compile("a.b")
m = p.match("a\nb")
print(m)

# 개행문자도 찾고싶다면 re에 있는 dotall 옵션을 사용하면 됨.
p = re.compile("a.b", re.DOTALL)
m = p.match("a\nb")
print(m)

p = re.compile("a.b")
m = p.match("axb")
print(m)
m = p.match("AxB")
print(m)  # none : 대문자는 포함을 안시킴.

p = re.compile("a.b", re.IGNORECASE)  # ignorecase 옵션을  주면 대소문자 구분없이 가능.
m = p.match("AxB")
print(m)

# multiline, M : 메타문자(^, $)와 관련된 옵션
p = re.compile(
    "^python\s\w+"
)  # 처음은 항상 python으로 시작해야하고 만약 python$이라면 항상 끝이 python이어야한다.
data = """python one
life is too short
python two
you need python
python three"""

print(p.findall(data))  # python one 만 출력

p = re.compile("^python\s\w+", re.M)  # 멀티라인을 사용하면 개행도 알아서 해서 읽음
print(p.findall(data))


# verbose, X
# charref = re.compile(r"&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F])+);")
# charref_x = re.compile(r"&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F])+);)", re.X)


data = r"\section section2 section3 \section4"
p = re.compile(r"\\section")
m = p.findall(data)
print(m)

text = """이름 : 김철수
전화번호 : 010-1234-234
나이 : 30
성별 : 남"""
print(re.findall("\d+", text))  # 숫자인 것
print(re.findall("\D+", text))  # 숫자가 아닌것
print(re.findall("\W+", text))  # 문자와 숫자가 아닌것


# 자주 쓰는 메타문자
# 메타문자	의미	예시	설명
# .	아무 문자 1개	a.c	abc, acc 등
# ^	문자열의 시작	^abc	abc로 시작하는 문자열
# $	문자열의 끝	abc$	abc로 끝나는 문자열
# *	0회 이상 반복	a*	"", "a", "aaaa"
# +	1회 이상 반복	a+	"a", "aaa"
# ?	0 또는 1회	a?	"", "a"
# {n}	n회 반복	a{3}	"aaa"
# {n,m}	n~m회 반복	a{2,4}	"aa", "aaa", "aaaa"
# []	문자 집합	[abc]	"a", "b", "c"
# `	`	OR	`abc
# ()	그룹	(ab)+	"ab", "abab" 등

# 자주 쓰는 이스케이프 시퀀스
# 패턴	의미	예시
# \d	숫자 (0~9)	\d{3} → 3자리 숫자
# \D	숫자 아님
# \w	문자 (a-z, A-Z, 0-9, _)
# \W	문자 아님
# \s	공백 문자 (띄어쓰기, 탭 등)
# \S	공백 아닌 문자
# \\	역슬래시 자체

# re 모듈 함수들
# 함수	설명
# re.search()	문자열에서 처음 일치하는 패턴을 찾음
# re.match()	문자열 시작부터 일치하는지 확인
# re.findall()	일치하는 모든 문자열을 리스트로 반환
# re.finditer()	일치하는 모든 Match 객체를 반환
# re.sub()	특정 패턴을 새 문자열로 바꿈
# re.compile()	정규표현식 패턴을 객체로 컴파일 (재사용 용이)
