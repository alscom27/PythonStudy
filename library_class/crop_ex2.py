from PIL import Image

img = Image.open("C:\\Users\\main\workspace\\20250331-python\\library_class\\june.png")
box = (76, 3, 156, 183)
crop_img1 = img.crop(box)

drop = (0, 3, 80, 183)
img.paste(crop_img1, drop)
img.show()

img2 = Image.open("C:\\Users\\main\workspace\\20250331-python\\library_class\\june.png")
crop_img2 = crop_img1.resize((40, 90))  # 축소
crop_img2.save("40x90june.png")
drop = (20, 40, 60, 130)
img2.paste(crop_img2, drop)

box = (80, 3, 180, 103)
crop_img3 = img2.crop(box).rotate(90)
drop = (220, 0, 320, 100)
img2.paste(crop_img3, drop)
img2.show()
