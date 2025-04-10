from PIL import Image, ImageFilter

img = Image.open("C:\\Users\\main\workspace\\20250331-python\\library_class\\june.png")
img1 = img.filter(ImageFilter.CONTOUR)
img1.save("june_contour.png")

img2 = img.filter(ImageFilter.EMBOSS)
img2.save("june_emboss.png")

img3 = img.filter(ImageFilter.SMOOTH_MORE)
img3.save("june_smooth_more.png")


rgb = img.split()
r, g, b = rgb[0], rgb[1], rgb[2]
img4 = Image.merge("RGB", (b, b, g))
img4.save("june_rgb.png")

img5 = Image.merge("RGB", (b, r, g))
img5.save("june_BRG.png")
