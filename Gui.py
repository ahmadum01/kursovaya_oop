from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.wm_state("zoomed")
root.title("Виселица")
root.call('tk', 'scaling', 2.0)

root_h = root.winfo_screenheight() #Высота экрана
root_w = root.winfo_screenwidth() #Ширина экрана

canvas = Canvas(root, width=root_w, height=root_h, bg="black")
canvas.place(x=0, y=0, anchor="nw")

#Установка фонового изображения
background_image=Image.open("kletka.png")
background_image = background_image.resize((root_w, root_h))
background_image = ImageTk.PhotoImage(background_image)
canvas.create_image(0, 0, image=background_image, anchor="nw")

#Однопиксельное изображение(костыль для более гибкого регулирования размеров кнопок)
pixelVirtual = PhotoImage(width=1, height=1)