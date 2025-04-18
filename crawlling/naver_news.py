import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import requests
from bs4 import BeautifulSoup

# 수정하고자 하는 메인 링크
link = "https://news.naver.com/breakingnews/section/101/310?date="
# 스크랩 학소 싶은 날짜를 년도월일 나열
date = "20250417"
# 메인 링크는 링크에 날짜가 붙은 구조이기 때문에 이렇게 작성함.
main_link = link + date
# 기사의 수, 제목, 링크를 받아올 예정이기 때문에 정보를 담아줄 데이터 프레임 생성.
Main_link = pd.DataFrame({"number": [], "title": [], "link": []})


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get(main_link)
# 웹 페이지 로딩을 기다리는 코드
time.sleep(3)

# 기사 더 보기가 몇 개가 있을지 모르기 때문에 오류가 날 때까지 누르는 것으로 함.
# 여기서 발생하는 오류란 버튼을 찾을 수 없다 즉, 버튼이 없을 때 발생하는 오류
while True:
    try:
        # 기사 더보기 버튼 클릭 후 계속 버튼 찾게 반복문 않에 넣음.
        # By.CLASS_NAME = 단일 클래스명만 가능(공백 없이), html 태그에 클래스가 여러 개 있어도 하나만 정확히 입력해야 작동
        # By.CSS_SELECTOR = CSS 선택자 문법 전체 지원, 복합 클래스, ID, 태그, 속성 등 모두 가능(.클래스1.클래스2 식으로 연결)
        more_btn = driver.find_element(
            By.CSS_SELECTOR, ".selection_more_inner._CONTENT_LIST_LOAD_MORE_BUTTON"
        )
        more_btn.click()
        time.sleep(3)
    except:
        print("더보기 버튼 없음")
        break

# 기사의 제목과 링크가 모두 담긴 a태그를 모두 찾는다
articles = driver.find_elements(By.CSS_SELECTOR, ".sa_text_title._NLOG_IMPRESSION")
# a태그 내 기사의 제목과 링크를 따로 저장
for i in range(len(articles)):
    # 기사의 제목
    # strip()을 사용하여 눈으로 확인할 수 없는 양 끝의 공백을 제거
    title = articles[i].text.strip()
    # href 부분을 가져오는 방법
    # a태그 내 href를 가져온다.
    link = articles[i].get_attribute("href")
    # 번호는 0부터 시작하기 때문에 1을 더해줌
    li = [i + 1, title, link]
    Main_link.loc[i] = li

print(Main_link)

# 엑셀을 잘 관리하기 위해서 크롤링 날짜를 파일 이름에 포함한다
excel_name = "news_" + date + ".xlsx"
with pd.ExcelWriter(excel_name) as writer:
    Main_link.to_excel(writer, sheet_name="링크", index=False)
    print(f"엑셀 저장 완료")

# 크롤링 완

# naver_news_detail

# 기존에 크롤링했던 결과물 엑셀파일
# 엑셀 파일의 이름은 첫 번째 코드에서 저장한 부분이기 때문에 코드마다 달라질 수 있다.
link = pd.read_excel("news_" + date + ".xlsx")

# 기사의 본문까지 포함한 크롤링 결과물을 저장할 엑셀 파일의 이름
# 파일 관리를 쉽게 하기 위해서 날짜를 넣었다.
excel_name = "news_detail_" + date + ".xlsx"

# 기사들의 링크를 리스트화
Main_link = list(link["link"])

# 기사의 수, 기사의 제목, 기사의 본문, 기사의 링크 정보를 담아줄 데이터 프레임을 생성한다.
Information = pd.DataFrame({"number": [], "title": [], "information": [], "link": []})

# 기사의 수, 기사의 제목, 기사의 링크는 이전 크롤링 결과물에 동일하게 존재하기 때문에 바로 정보를 담는다.
Information["number"] = link["number"]
Information["title"] = link["title"]
Information["link"] = link["link"]

# 기사 본문을 담을 변수
information = []

# 각각의 기사 링크에서 본문 가져오기
for link_url in Main_link:
    try:
        # 유효한 http/https 링크인지 확인
        if not str(link_url).startswith("http"):
            print(f"잘못된 URL 무시: {link_url}")
            information.append("잘못된 링크")
            continue

        # headers={'User-Agent' : 'Mozilla/5.0'} : 이걸 안넣으면 로봇인줄 알고 html을 안 보내줄 수도 있음.
        response = requests.get(link_url, headers={"User-Agent": "Mozilla/5.0"})

        if response.status_code == 200:
            html = response.content
            soup = BeautifulSoup(html, "html.parser")
            article_div = soup.find("div", {"id": "newsct_article"})

            if article_div:
                # 엑셀 내 칸을 크게 차지하는 것을 방지하기 위해 줄바꿈을 띄어쓰기로 변경
                # 크롤링에서 필요한 코드는 아니라 생략해도 무관
                info = article_div.text.strip().replace("\n", " ")

                # 기자의 정보가 '기사제공' 이후부터 나오기 때문에 전체 본문에서 해당 글을 찾는다.
                if "기사제공" in info:
                    end = info.index("기사제공")
                    # '기사제공' 이전에 등장하는 문자 즉, 기사의 본문만 변수에 저장하여, 본문과 기자를 분리한다.
                    info = info[:end]
                information.append(info)

            else:
                information.append("본문 없음")
        else:
            information.append("응답 실패")
    except Exception as e:
        information.append(f"에러: {str(e)}")

with pd.ExcelWriter(excel_name) as writer:
    Information.to_excel(writer, sheet_name="결과값", index=False)
    print("저장 완료")

# 안된거같은데 셀레니움으로 클릭해서 들어가야되는거아닌가?
