from PIL import Image, ImageTk
import tkinter as tk, ImageFilter

# 윈도우를 생성하고 윈도우 안에 캔버스를 생성
window = tk.Tk()
canvas = tk.Canvas(window, width=500, height=500)
canvas.pack()

img = Image.open("C:\\Users\\main\workspace\\20250331-python\\library_class\\lenna.png")
# img = Image.open(
#     "C:\\Users\\main\workspace\\20250331-python\\library_class\\magiceye.jpg"
# )


# 45도 회전 (시계반대방향으로)
# out = img.rotate(45)

out = img.filter(ImageFilter.BLUR)

# tk 형식으로 영상을 변환한다
tk_img = ImageTk.PhotoImage(out)
# tk_img = ImageTk.PhotoImage(img)

canvas.create_image(250, 250, image=tk_img)
window.mainloop()
