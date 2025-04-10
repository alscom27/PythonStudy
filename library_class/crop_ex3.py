from PIL import Image

img4 = Image.open("C:\\Users\\main\workspace\\20250331-python\\library_class\\june.png")

box = (76, 3, 156, 333)
crop4 = img4.crop(box)
crop_img4 = crop4.transpose(Image.FLIP_LEFT_RIGHT)
drop = (0, 3, 80, 333)
img4.paste(crop_img4, drop)
img4 = img4.transpose(Image.FLIP_LEFT_RIGHT)
img4.show()
