from PIL import Image

img = Image.open("C:\\Users\\main\workspace\\20250331-python\\library_class\\june.png")

print(img.format, img.size, img.mode)
img.show()
# 이미지 자르기
box = (78, 3, 156, 183)
crop_img = img.crop(box)
crop_img.save(
    "june_torch.png"
)  # 워크스페이스가 기본디렉토리로 잡혀있는지 워크스페이스에 사진저장됨.
print(crop_img.format, crop_img.size, crop_img.mode)
crop_img.show()
