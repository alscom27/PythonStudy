# matplotlib : 파이썬에서 자료를 차트나 플롯으로 시각화하는 패키지
# pyplot : 데이터 시각화를 위한 기본 서브 패키지

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

# plt의 plot() 함수는 리스트 자료값을 y 값으로 삼아 화면의 그려주는 일을 함.
# 이 때 x값의 범위는 생략이 가능하고 디폴트는 [0,1,...n] n은 y값 개수에 의해 결정
# plt.plot([1, 2, 3, 4])
# plt.ylabel("y label")  # 각 축의 레이블을 적음. 각 축의 속성기록용
# plt.xlabel("x label")
# plt.show()  # 화면에 그래프를 그려주는 일

# x = np.arange(10)
# plt.plot(x**2)
# plt.axis([0, 100, 0, 100])  # axis : x축 y축 범위를 지정할 수 있음.
# # plt.show()

x = np.arange(-20, 20)  # -20에서 20사이의 수를 1의 간격으로 생성.
y1 = 2 * x
y2 = (1 / 3) * x**2 + 5
y3 = -(x**2) - 5

# 녹색 점선, 빨간 실선에 세모, 파란 점들과 별표로 함수 표현
plt.plot(x, y1, "g--", x, y2, "r^-", x, y3, "b*:")
plt.axis([-30, 30, -30, 30])
plt.show()

x = np.arange(50)
y = np.random.random(50)
plt.plot(x, y, "g^:")
plt.show()
