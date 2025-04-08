"""
정사각형 속성 계산 모듈
"""

# """이렇게하면 모듈 임포트할때 설명 표시됨 """
xpos, ypos = 0, 0


def get_area(length):
    """
    정사각형의 면적을 구하는 함수
    """
    return length**2


def get_peri(length):
    return length * 4
