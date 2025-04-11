import numpy as np
import matplotlib.pyplot as plt

# IPython.displat 서브 모듈에 있는 Image 객체를 사용해서 파일의 내용을 화면의 출력하는 기능
# python에서는 안되고 주피터 노트북에서만 되는듯...?
from IPython.display import Image

x = np.linspace(0, np.pi * 2, 100)  # 2*pi는 360도에 해당함
fig = plt.figure()  # 이미지로 저장하기 위해 plt의 figure객체 생성
plt.plot(x, np.sin(x), "r-")
plt.plot(x, np.cos(x), "b:")
fig.savefig("sin_cos_fig.png")  # 이미지로 저장
# plt.show()
