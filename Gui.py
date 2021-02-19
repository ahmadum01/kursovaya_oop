from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.wm_state("zoomed")
root.title("")
root.call('tk', 'scaling', 2.0)


root_h = root.winfo_screenheight()
root_w = root.winfo_screenwidth()

#Установка фонового изображения
background_image=Image.open("kletka.png")
background_image = background_image.resize((root_w, root_h))
background_image = ImageTk.PhotoImage(background_image)
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)