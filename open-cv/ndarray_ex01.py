import cv2

img1 = cv2.imread("cat.bmp", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("cat.bmp", cv2.IMREAD_COLOR)
print(
    f"img1(gray) ndim : {img1.ndim} , shape : {img1.shape} , size : {img1.size} , dtype : {img1.dtype}"
)
print(
    f"img2(color) ndim : {img2.ndim} , shape : {img2.shape} , size : {img2.size} , dtype : {img2.dtype}"
)

# 파이썬에서랑 주피터에서 실행할때 찾아오는 경로가 다른가봄?
