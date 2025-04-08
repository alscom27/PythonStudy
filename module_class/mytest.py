import mycircle0
import myrect0
import mysquare
import modl

# 반지름이 5일 때의 면적, 둘레를 구하고 x, y 위치를 100, 100으로 보내기
radius = 5
circle_area = mycircle0.get_area(radius)
circle_peri = mycircle0.get_peri(radius)
mycircle0.set_pos(100, 100)
print(
    f"반지름 {radius}의 원의 면적은 : {circle_area:0.2f}, 둘레는 : {circle_peri:0.2f}"
)

# 너비가 3이고 높이가 4인 직사각형의 면적, 둘레를 구하고 x,y위치를 200,200으로 설정
width = 3
height = 4
rect_area = myrect0.get_area(width, height)
rect_peri = myrect0.get_peri(width, height)
myrect0.set_pos(200, 200)
print(
    f"너비가 {width}고 높이가 {height}인 직사각형의 면적은 : {rect_area}, 둘레는 {rect_peri}"
)

square_area = mysquare.get_area(50)
print(f"한 변의 길이가 50인 정사각형의 면적은 : {square_area}")
print(mysquare.__doc__)
# 모듈의 설명이 나옴 """"""


print(modl.sum(3, 4))
print(modl.safe_sum(3, 4))
print(modl.safe_sum(1, "a"))
