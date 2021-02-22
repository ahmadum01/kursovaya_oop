#Игра виселица
import random
from Gui import *

class Letter():
    def __init__(self, master, width, height, letter=None, font_size=10):
        w, h, bd = root_w / 15, int(root_w / 15 * (110 / 140)), int(root_w / 40 / 14)
        self.frame = Frame(master, width=w, height=h, bg="black", bd=bd)
        self.label = Label(self.frame, 
            width=width, 
            height=height, 
            font=f"Tahoma {font_size} bold", 
            bg="white",
            fg = "red"
        )
        self.label.place(width=w - bd * 2, height=h - bd * 2)
        self.letter = letter

    def show(self):
        self.label['text'] = self.letter

canvas.create_line(root_w/2, root_h/2-root_h/40, #Виселица
    root_w/2 - root_w/10, root_h/2-root_h/40, 
    root_w/2 - root_w/20, root_h/2-root_h/40,
    root_w/2 - root_w/20, root_h/2-root_h/40-root_h/2.5,
    root_w/2 - root_w/20 + root_w/6, root_h/2-root_h/40-root_h/2.5,
    root_w/2 - root_w/20 + root_w/20, root_h/2-root_h/40-root_h/2.5,
    root_w/2 - root_w/20, root_h/2-root_h/40-root_h/2.5 + root_w/20,
    root_w/2 - root_w/20 + root_w/20, root_h/2-root_h/40-root_h/2.5,
    root_w/2 - root_w/20 + root_w/6, root_h/2-root_h/40-root_h/2.5,
    root_w/2 - root_w/20 + root_w/6, root_h/2-root_h/40-root_h/2.5 + root_h/9,
    width=10,
)

canvas.create_oval(root_w/2 - root_w/20 + root_w/6-root_w/40, root_h/2-root_h/40-root_h/2.5 + root_h/9,
    root_w/2 - root_w/20 + root_w/6+root_w/40, root_h/2-root_h/40-root_h/2.5 + root_h/9+root_w/20,
    width=10
)

class Counter(Label):
    def __init__(self, master, font_size, name):
        super().__init__(master, font=f"Tahoma {font_size}")
        self.name = name

def check(value, letters, word):
    if value in word:
        for i in letters:
            if i.letter == value:
                i.show()


def push(event):
    check(event.widget["text"], letters, word)
    event.widget.grid_forget()

all_words = ["программа", "питон", "переменная", "функция", 
                "класс", "метод", "объект", "атрибут","список","массив"]

if __name__ == '__main__':
    word = random.choice(all_words).upper()
    word_frame = Frame(root, bd=3, bg="black")
    word_frame.place(relx=0.5, rely=0.6, anchor="center")
    letters = [Letter(word_frame, 1, 1, i, 30) for i in word.upper()]
    for i in range(len(letters)):
       letters[i].frame.grid(row=0, column=i)

    #Создание кнопок
    buttons = []
    buttons_frame = Frame(root, bg="white")
    buttons_frame.place(relx=0.5, rely=0.85, anchor="center")
    for i in "АБВГДЕЁЖЗИЙКЛМНОПРСТУФXЦЧШЩЪЫЬЭЮЯ":
        buttons.append(Button(buttons_frame, 
                text=i, font="Tahoma 16 bold", 
                bg="black", 
                image=pixelVirtual, 
                width=75, 
                compound="c", 
                fg="white",
                bd=0,
            )
        )
    
    #Расположение алфавита
    for i in range(3):
        for j in range(11):
            buttons[i*10+j+i].grid(row=i, column=j, padx=10, pady=5)

    #События
    for i in buttons: i.bind("<Button-1>", push)

    #Главный цикл
    root.mainloop()