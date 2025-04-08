import math

PI = math.pi
xpos, ypos = 0, 0  # 전역 변수


def get_area(radius):
    return PI * radius**2


def get_peri(radius):
    return 2 * PI * radius


# global : 전역 변수 느낌?
def set_pos(x, y):
    global xpos, ypos
    xpos, ypos = x, y
