# gpt가 만들어준 문제

# 도전


# 계속, 종료 메뉴
def menu_se():
    print("=" * 20)
    print(
        """1. 계속
2. 종료"""
    )
    print("=" * 20)


# 커서(사용자가 메뉴 번호를 입력) 예외 처리
# 메서드 안에 매개변수로 메서드가 가능
def cursor_func(menu_func):
    while True:
        menu_func()
        try:
            cursor = int(input("메뉴 번호를 입력해주세요. "))
        except ValueError:
            print("잘 못 입력했습니다. 숫자를 입력해주세요.")
            continue
        break
    return cursor


# 1. 단어 빈도수 세기
# 입력된 문장에서 각 단어가 몇 번 나왔는지 딕셔너리로 정리
# + 한글, 영어 | 단어 외에 부사 접속사 조사 등등 나눠서 카운트 정리

# 영어에서는 띄어쓰기 기준으로 단어를 나누는 게 일반적입니다.

# 예:
# I'm eating an apple → ["I'm", "eating", "an", "apple"] → 4단어

# ※ 보통 I'm처럼 축약된 형태도 하나의 단어로 봅니다.
# ※ "an", "the", "a" 같은 관사나 "is", "am", "are" 같은 be동사도 모두 단어로 셉니다.

# 조사 종류     주요 조사들                     의미
# 주격 조사	    이, 가	                        주어 역할
# 목적격 조사	을, 를	                        목적어 역할
# 보격 조사	    이, 가	                        보어 역할
# 관형격 조사	의	                            ~의 관계
# 부사격 조사	에, 에서, 으로, 로, 까지 , 부터, 처럼 등	    부사처럼 부연 설명
# 보조사	    은, 는, 도, 만, 조차, 마저 등	강조, 비교 등 느낌 전달

# + 한글은 konlpy를 사용해보는데 신기해서 감정 분석 기능 추가


def word_frequency():
    import re

    # pip install langdetect : 문장 전체 영어와 한글 판별을 위해 외부라이브러리 설치
    from langdetect import detect

    # 파이썬에서 일반 딕셔너리는 존재하지 않는 키를 조회하면 KeyError 발생
    # defaultdict 자동으로 기본값을 설정
    from collections import defaultdict

    # pip install konlpy
    # + Java 기반으로 동작하는 분석기를 사용하기 때문에 JVM필요
    # 그래서 자바 설치하고 환경변수 잡음 (JDK 8버전이 제일 안정적)
    # konlpy : 한국어 형태소 분석을 파이썬에서 할 수 있게 해주는 오픈소스 NLP(자연어 처리) 라이브러리
    # 문장에서 단어 추출, 조사 분리, 품사 태깅, 명사만 추출 등을 함
    from konlpy.tag import Okt

    while True:
        print("단어 빈도수 세기")

        cursor = cursor_func(menu_se)

        if cursor == 1:
            while True:
                user_string = input("문장을 입력해주세요 : ")
                word_dict = dict()
                # langdetect 영어면 'en' 한글이면 'ko' 반환
                if detect(user_string) == "en" and len(user_string) != 0:
                    # 영어 문장은 띄어쓰기로 단어 구분
                    # don't나 it's의 '는 인식하되 ., !구분점은 제거
                    word_list = re.findall(r"\b[\w']+\b", user_string)
                    # 모든 밸류가 0이고 키값이 word_list인 딕셔너리로 변환
                    word_dict = dict.fromkeys(word_list, 0)

                    for word in word_list:
                        for key in word_dict:
                            if word == key:
                                word_dict[word] += 1

                    print(f"{'단어':^8} | {'횟수':^7}")
                    for word_key in word_dict.keys():
                        print(f"{word_key:^10} | {word_dict[word_key]:^10}")

                    break

                elif detect(user_string) == "ko" and len(user_string) != 0:
                    # 한글은 조사도 구분
                    okt = Okt()  # 형태소 분석기 객체 선언
                    # pos() : 텍스트를 형태소 단위로 나누고, 품사 태깅을 해주는 메서드
                    # stem=True : 동사,형용사를 원형(기본형) 으로 바꿔줌
                    # (단어, 품사)가 들어있는 튜플의 리스트로 반환
                    tokens = okt.pos(user_string, stem=True)

                    # 기본값이 정수(0)인 딕셔너리
                    word_dict = defaultdict(int)
                    josa_dict = defaultdict(int)

                    # 감정분석 기능 추가를 위한 긍정, 부정 키워드 집합
                    positive_words = {
                        "좋다",
                        "행복하다",
                        "기쁘다",
                        "즐겁다",
                        "사랑",
                        "맛있다",
                        "예쁘다",
                        "감사",
                    }
                    negative_words = {
                        "싫다",
                        "슬프다",
                        "짜증나다",
                        "화나다",
                        "별로",
                        "불쾌하다",
                        "미워",
                        "지루하다",
                    }

                    score = 0

                    for word, tag in tokens:
                        # token = (word, tag)
                        # 단어가 조사 라면
                        if tag == "Josa":
                            josa_dict[word] += 1
                        # 명사, 동사, 형용사 라면
                        elif tag in ["Noun", "Verb", "Adjective"]:
                            word_dict[word] += 1
                            # 감정 분석 기능 추가
                            if word in positive_words:
                                score += 1
                            elif word in negative_words:
                                score -= 1

                    print(f"단어 : {dict(word_dict)}")
                    print(f"조사 : {dict(josa_dict)}")

                    if score > 0:
                        print(f"😊 오늘 기분이 좋은신가봅니다!")
                    elif score < 0:
                        print(f"😡 오늘 기분이 나쁘신가봅니다..")
                    else:
                        print(f"😐 오늘 평범한 하루를 보내시는가 봅니다.")

                    break

                elif len(user_string) == 0:
                    # 아무것도 입력하지 않았을 때
                    print("아무것도 입력하지 않았습니다. 다시 입력해주세요.")
                    continue

                else:
                    print("판별할 수 없는 문장입니다. 다시 입력해주세요.")
                    continue

        elif cursor == 2:
            print("단어 빈도수 세기를 종료합니다.")
            break
        else:
            print("없는 메뉴입니다. 다시 선택해주세요.")
            continue


# 3. 날짜 차이 계산기
# datetime 모듈로 두 날짜 간 차이 구하기
# import : 모듈 전체를 가져옴, 사용할 때마다 모듈이름.함수명()으로 접근 가능
# from import : 모듈 안에서 특정 함수, 클래스만 골라서 가져옴, 사용할 때 함수만 호출 가능


def fixed_input(user_input):
    import re

    # 한글 → 기호 기반 변환 (전처리)
    user_input = re.sub(r"[년월일]", " ", user_input).strip()
    user_input = re.sub(r"\s+", " ", user_input)  # 여러 공백 → 하나로
    return user_input


def parse_date(user_date):
    from datetime import datetime

    # 가능한 날짜 포맷 리스트
    formats = [
        "%Y년 %m월 %d일",
        "%Y/%m/%d",
        "%Y-%m-%d",
        "%Y.%m.%d",
        "%Y %m %d",
        "%Y%m%d",
    ]
    parsed_date = None
    for fmt in formats:
        try:
            parsed_date = datetime.strptime(user_date, fmt)
            break
        except ValueError:
            parsed_date = -1
    return parsed_date


def date_diff_func():
    # datetime의 strptime()은 모듈에 있는게아니라 datetime 클래스에 있는것이므로 import datetime으로 부를 수 없음.
    # import datetime
    from datetime import datetime

    while True:
        print("날짜 차이 계산기")

        cursor = cursor_func(menu_se)

        if cursor == 1:
            while True:

                input_date1 = input("첫번째 날짜를 입력해주세요. ")
                input_date2 = input("두번째 날짜를 입력해주세요. ")
                fixed_date1 = fixed_input(input_date1)
                fixed_date2 = fixed_input(input_date2)

                parsed_date1 = parse_date(fixed_date1)
                parsed_date2 = parse_date(fixed_date2)

                if parsed_date1 == -1 or parsed_date2 == -1:
                    print("날짜 형식을 인식할 수 없습니다. 다시 입력해주세요.")
                    continue

                else:
                    date_diff = abs(parsed_date1 - parsed_date2)
                    print(f"두 날짜의 차이는 {date_diff} 입니다.")
                    break

        elif cursor == 2:
            print("날짜 차이 계산기를 종료합니다.")
            break
        else:
            print("없는 메뉴입니다. 다시 선택해주세요.")
            continue


# 2. json 파일에서 데이터 읽고 가공하기
# json 모듈 사용해서 데이터 불러오고, 필터링/출력
# +
# 4. 간단한 채팅 봇 만들기
# if-elif-else로 사용자의 입력에 반응하는 간단한 챗봇 만들기
# 2번 4번을 합쳐서 ___ 데이터를 이용한 챗봇으로 만들기로 변경


# 파이썬에서 HTTP 요청을 보낼 때는 requests 라이브러리를 많이 사용함.
# pip install requests
# 71efe28b43424ed79f88
def json_chat_bot():
    import requests
    from konlpy.tag import Okt

    while True:
        print("레시피 추천 챗봇")

        cursor = cursor_func(menu_se)

        if cursor == 1:

            ###################### json 파싱 ######################
            # 인증키
            service_key = "71efe28b43424ed79f88"
            # API 요청 주소
            #         api요청 주소                           /인증키/요청데이터/데이터타입/시작 인덱스/끝 인덱스
            url = f"http://openapi.foodsafetykorea.go.kr/api/{service_key}/COOKRCP01/json/1/100"

            # 요청 보내기
            response = requests.get(url)

            # 응답 확인
            #  http 상태코드 200(성공) 이면
            if response.status_code == 200:
                # 딕셔너리
                data = response.json()

                # 레시피 리스트 꺼내기
                # data dict에서 key가 COOKRCP01인 값을 꺼내고, 꺼낸 값도 또 다른 딕셔너리거나 리스트라면 다시 key가 b인 값을 꺼냄
                items = data["COOKRCP01"]["row"]

                # 반복문으로 껍데기 벗겨가면서 값 출력하기
                # for item in items:
                #     print("요리명 :", item["RCP_NM"])
                #     print("재료:", item["RCP_PARTS_DTLS"])
                #     print("조리법 요약:", item["RCP_WAY2"])
                #     print("이미지 링크:", item["ATT_FILE_NO_MAIN"])
                #     print("=" * 40)
                # json 출력 test 성공
                ###################### /json 파싱 ######################

            else:
                print("API 요청 실패 :", response.status_code)
                break

            while True:
                print("=" * 40)
                print("대화를 입력해주세요.")
                user_input = input("사용자 : ")

                # 종료를 위한 키워드들
                end_list = [
                    "종료",
                    "그만",
                    "끝",
                    "나가기",
                    "닫기",
                    "exit",
                    "quit",
                    "bye",
                    "stop",
                    "그만하다",
                    "종료하다",
                ]

                if any(end_word in user_input.lower() for end_word in end_list):
                    print("챗봇 : 대화를 종료합니다.")
                    # 프로그램 즉시 종료
                    exit()

                okt = Okt()
                tokens = okt.pos(user_input, stem=True)

                # 키워드 분류
                # 명사와 동사만 구분
                nouns = [word for word, tag in tokens if tag == "Noun"]
                verbs = [word for word, tag in tokens if tag == "Verb"]

                # 형태소 분석기가 분석한 굽다와 데이터의 굽기 등 매치가 되지않아서 수정
                # verb[-1].replace('다', '기') 이 방법을 사용하려다가 replace는 문자열 전체를 수정해서 혹시 몰라 수정
                verb_methods = [
                    verb[:-1] + "기" for verb in verbs if verb.endswith("다")
                ]

                # 매치 점수 저장 리스트
                scored_items = []

                # 데이터 돌면서 매치 점수 계산
                for item in items:
                    score = 0
                    name = item["RCP_NM"]
                    ingredient = item["RCP_PARTS_DTLS"]
                    method = item["RCP_WAY2"]

                    # 음식명과 명사 키워드가 일치시
                    # any() : 리스트나 튜플 안에 있는 값 중 하나라도 true면 true
                    if any(noun in name for noun in nouns):
                        score += 1
                    # 재료에 명사 키워드가 일치시
                    if any(noun in ingredient for noun in nouns):
                        score += 1
                    # 요리 방법에 동사 키워드 일치시
                    if any(verb_method in method for verb_method in verb_methods):
                        score += 1

                    # 점수가 0보다 큰 건(언급이 된건) 리스트로 전부 등록
                    if score > 0:
                        scored_items.append((score, item))

                # 높은 점수 순으로 정렬
                # 키를 기준으로 내림차순
                scored_items.sort(key=lambda x: x[0], reverse=True)

                #  결과 5개만 선택해서 출력
                top_items = scored_items[:5]

                # 추천 레시피가 없으면
                if bool(top_items) == False:
                    print("추천드릴 레시피가 없습니다.")
                    continue

                print(
                    f"""챗봇 :
추천 요리 TOP 5"""
                )
                for score, item in top_items:
                    # print("=" * 40)
                    print("매치 점수 :", score)  # 확인용
                    print(f"요리명 : {item['RCP_NM']}")
                    print(f"재료 : {item['RCP_PARTS_DTLS']}")
                    print(f"조리법 : {item['RCP_WAY2']}")
                    print("=" * 40)

        elif cursor == 2:
            print("레시피 추천 챗봇을 종료합니다.")
            break
        else:
            print("없는 메뉴입니다. 다시 선택해주세요.")
            continue
