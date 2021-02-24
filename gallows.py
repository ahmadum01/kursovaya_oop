#Игра виселица
import random
import time
from tkinter import *
from PIL import Image, ImageTk


class App(Tk):
    def __init__(self):
        super().__init__()
        self.wm_state("zoomed")
        self.title("Виселица")
        self.call('tk', 'scaling', 2.0)
        self.root_h = self.winfo_screenheight() # Высота экрана
        self.root_w = self.winfo_screenwidth() # Ширина экрана
        # Создание виджета канвас
        self.canvas = Canvas(self, width=self.root_w, height=self.root_h, bg="black")
        self.canvas.place(x=0, y=0, anchor="nw")

        # Установка фонового изображения
        self.background_image = ImageTk.PhotoImage(Image.open("kletka.png").resize((self.root_w, self.root_h)))
        self.canvas.create_image(0, 0, image=self.background_image, anchor="nw")      
        # Однопиксельное изображение(костыль для более гибкого регулирования размеров кнопок)
        self.pixelVirtual = PhotoImage(width=1, height=1)    
        # Счетчик
        self.count = 0
        # Список слов    
        self.all_words = ["программа", "питон", "переменная", "функция", "класс", "метод", "объект", "атрибут","список","массив"]
        # Слово
        self.word = random.choice(self.all_words).upper()
        # Фрейм слова
        self.word_frame = Frame(self, bd=3, bg="black")
        self.word_frame.place(relx=0.5, rely=0.6, anchor="center")
        # Загаданные буквы
        self.letters = [Letter(self.word_frame, self.root_w, self.root_h, i, 30) for i in self.word]
        # print(self.letters, "вот")
        for i in range(len(self.letters)):
            self.letters[i].frame.grid(row=0, column=i)
        # Адреса к рисункам
        self.gallows_ = self.rope_ = self.head_ = self.l_leg_ = self.r_leg_ = self.body_ = self.r_hand_ = self.l_hand_ = None
        # Создание клавиатуры
        self.buttons = []
        self.buttons_frame = Frame(self, bg="white")
        self.buttons_frame.place(relx=0.5, rely=0.85, anchor="center")
        for i in "АБВГДЕЁЖЗИЙКЛМНОПРСТУФXЦЧШЩЪЫЬЭЮЯ":
            self.buttons.append(Button(self.buttons_frame, 
                    text=i, font="Tahoma 16 bold", 
                    bg="black", 
                    image=self.pixelVirtual, 
                    width=75, 
                    compound="c", 
                    fg="white",
                    bd=0,
                )
            )
        # Расположение клавиатуры
        for i in range(3):
            for j in range(11):
                self.buttons[i*10+j+i].grid(row=i, column=j, padx=10, pady=5)
        # Кнопка перезапуска игры
        self.reset_png = ImageTk.PhotoImage(Image.open("reset.png").resize((int(self.root_w/25), int(self.root_w/25))))
        self.reset_button = self.canvas.create_image(5, 5, image=self.reset_png, anchor="nw")
        # Создание счетчика
        self.score = Counter(self, "ОЧКИ", self.pixelVirtual)
        self.score.place(100, 140, 1, 0)

    def gallows(self):
        '''Рисует виселицу'''
        self.canvas.delete(self.gallows_,self.rope_)
        self.canvas.delete(self.gallows_,self.rope_)
        self.gallows_ = self.canvas.create_line(self.root_w/2-self.root_w/32, self.root_h/2 - self.root_h/40,
            self.root_w/2 - self.root_w/10-self.root_w/32, self.root_h/2 - self.root_h/40, 
            self.root_w/2 - self.root_w/20 - self.root_w/32, self.root_h/2 - self.root_h/40,
            self.root_w/2 - self.root_w/20-self.root_w/32, self.root_h/2-self.root_h/40-self.root_h/2.5,
            self.root_w/2 - self.root_w/20 + self.root_w/6-self.root_w/32, self.root_h/2-self.root_h/40-self.root_h/2.5,
            self.root_w/2 - self.root_w/20 + self.root_w/20-self.root_w/32, self.root_h/2-self.root_h/40-self.root_h/2.5,
            self.root_w/2 - self.root_w/20-self.root_w/32, self.root_h/2-self.root_h/40-self.root_h/2.5 + self.root_w/20,
            self.root_w/2 - self.root_w/20 + self.root_w/20-self.root_w/32, self.root_h/2-self.root_h/40-self.root_h/2.5,
            width=10,
        )
        self.rope_ = self.canvas.create_line(self.root_w/2 - self.root_w/20 + self.root_w/6-self.root_w/32, self.root_h/2-self.root_h/40-self.root_h/2.5,
            self.root_w/2 - self.root_w/20 + self.root_w/6-self.root_w/32, self.root_h/2-self.root_h/40-self.root_h/2.5 + self.root_h/9,
            width=6
        )

    def head(self):
        '''Рисует голову'''
        self.canvas.delete(self.head_)
        self.head_ = self.canvas.create_oval(self.root_w/2 - self.root_w/20 + self.root_w/6-self.root_w/42-self.root_w/32, self.root_h/2-self.root_h/40-self.root_h/2.5 + self.root_h/9,
        self.root_w/2 - self.root_w/20 + self.root_w/6+self.root_w/42-self.root_w/32, self.root_h/2-self.root_h/40-self.root_h/2.5 + self.root_h/9+self.root_w/20,
        width=5
    )  

    def body(self):
        '''Рисует тело'''
        self.canvas.delete(self.body_)
        self.body_ = self.canvas.create_line(self.root_w/2 - self.root_w/20 + self.root_w/6-self.root_w/32, self.root_h/2-self.root_h/40-self.root_h/2.5 + self.root_h/9+self.root_w/20,
            self.root_w/2 - self.root_w/20 + self.root_w/6-self.root_w/32, self.root_h/2-self.root_h/40-self.root_h/2.5 + self.root_h/9+self.root_w/9,
            width=5
        )

    def l_hand(self):
        '''Рисует левую руку'''
        self.canvas.delete(self.l_hand_)
        self.l_hand_ = self.canvas.create_line(self.root_w/2 - self.root_w/20 + self.root_w/6-self.root_w/32, self.root_h/2-self.root_h/40-self.root_h/2.5 + self.root_h/9+self.root_w/19,
            self.root_w/2 - self.root_w/20 + self.root_w/6- self.root_w/30-self.root_w/32, self.root_h/2-self.root_h/40-self.root_h/2.5 + self.root_h/9+self.root_w/21+self.root_w/30,
            width=5
        )

    def r_hand(self):
        '''Рисует правую руку'''
        self.canvas.delete(self.r_hand_)
        self.r_hand_ = self.canvas.create_line(self.root_w/2 - self.root_w/20 + self.root_w/6-self.root_w/32, self.root_h/2-self.root_h/40-self.root_h/2.5 + self.root_h/9+self.root_w/19,
            self.root_w/2 - self.root_w/20 + self.root_w/6 + self.root_w/30-self.root_w/32, self.root_h/2-self.root_h/40-self.root_h/2.5 + self.root_h/9+self.root_w/21+self.root_w/30,
            width=5
        )

    def l_leg(self):
        '''Рисует левую ногу'''
        self.canvas.delete(self.l_leg_)
        self.l_leg_ = self.canvas.create_line(self.root_w/2 - self.root_w/20 + self.root_w/6-self.root_w/32, self.root_h/2-self.root_h/40-self.root_h/2.5 + self.root_h/9+self.root_w/9-self.root_h/200,
            self.root_w/2 - self.root_w/20 + self.root_w/6 - self.root_w/30-self.root_w/32, self.root_h/2-self.root_h/40-self.root_h/2.5 + self.root_h/9+self.root_w/9+self.root_w/30,
            width=5
        )

    def r_leg(self):
        '''Рисует правую ногу'''
        self.canvas.delete(self.r_leg_)
        self.r_leg_ = self.canvas.create_line(self.root_w/2 - self.root_w/20 + self.root_w/6-self.root_w/32, self.root_h/2-self.root_h/40-self.root_h/2.5 + self.root_h/9+self.root_w/9-self.root_h/200,
            self.root_w/2 - self.root_w/20 + self.root_w/6 + self.root_w/30-self.root_w/32, self.root_h/2-self.root_h/40-self.root_h/2.5 + self.root_h/9+self.root_w/9+self.root_w/30,
            width=5
        )

    def check(self, value):
        '''Проверяет на правильность введенную букву'''
        if value in self.word:
            self.score.increment()
            for i in self.letters:
                if i.letter == value: 
                    i.show()
        else:
            if self.count == 0:
                self.gallows()
            elif self.count == 1:
                self.head()
            elif self.count == 2:
                self.body()
            elif self.count == 3:
                self.l_hand()
            elif self.count == 4:
                self.r_hand()
            elif self.count == 5:
                self.l_leg()
            elif self.count == 6:
                self.r_leg()
            self.count += 1

        if self.isWin():
            self.reset("победа")
        if  self.isLose():
            for i in self.buttons:
                i['state'] = 'disabled'
                i.unbind("<Button-1>")

    def reset(self, event):
        '''Перезагружет игру'''
        for i in self.letters:
            i.frame.grid_forget()
            i.label.place_forget()
        forget("a", *self.buttons)
        self.word_frame.place_forget()
        self.change_word()
        self.word_frame = Frame(self, bd=3, bg="black")
        self.word_frame.place(relx=0.5, rely=0.6, anchor="center")

        self.letters = [Letter(self.word_frame, self.root_w, self.root_h, i, 30) for i in self.word]
        for i in range(len(self.letters)):
            self.letters[i].frame.grid(row=0, column=i)
        for i in range(3):
            for j in range(11):
                self.buttons[i*10+j+i].grid(row=i, column=j, padx=10, pady=5)
        self.buttons_frame.place(relx=0.5, rely=0.85, anchor="center")
        self.count = 0
        self.wanish()
        for i in self.buttons:
            i['state'] = 'normal'
            i.bind("<Button-1>", MyApp.push)
        if event != 'победа':
            self.score.reset()

    def change_word(self):
        '''Меняет слово'''
        self.word = random.choice(self.all_words).upper()

    def isWin(self):
        '''Проверяет угадано ли слово'''
        for i in self.letters:
            if not i.active:
                return False
        return True
    
    def isLose(self):
        '''Проверяет не помер ли человечик)'''
        if self.count == 7:
            return True


    def push(self, event):
        '''Удаляет использованные клавиши с буквами'''
        event.widget.grid_forget()
        self.check(event.widget["text"])

    def wanish(self):
        self.canvas.delete(self.gallows_,self.rope_, self.head_, self.l_leg_, self.r_leg_, self.body_, self.r_hand_, self.l_hand_)


class Letter():
    def __init__(self, master, root_w, root_h, letter=None, font_size=10):
        w, h, bd = root_w / 15, int(root_w / 15 * (110 / 140)), int(root_w / 40 / 14)
        self.frame = Frame(master, width=w, height=h, bg="black", bd=bd)
        self.label = Label(self.frame,
            font=f"Tahoma {font_size} bold", 
            bg="white",
            fg = "red"
        )
        self.label.place(width=w - bd * 2, height=h - bd * 2)
        self.letter = letter
        self.active = False

    def show(self):
        self.label['text'] = self.letter
        self.active = True


class Counter():
    def __init__(self, master, name, pixelVirtual):
        self.name = name
        self.value = 0
        self.frame = Frame(master)
        self.label = Label(self.frame, font="Tahoma 25", text=str(self.value),  image=pixelVirtual, compound="c", bg='black', fg='red')
        self.sign = Label(self.frame, font="Tahoma 20", text=self.name, image=pixelVirtual, compound="c", bg='black', fg="white")

    def place(self, width, height, relx, rely):
        self.label["width"] = width
        self.label["height"] = width
        self.sign["width"] = width
        self.sign["height"] = height - width
        self.sign.pack()
        self.label.pack()
        self.frame.place(relx=relx, rely=rely, anchor='ne')

    def increment(self):
        self.value += 1
        self.label['text'] = str(self.value)

    def reset(self):
        self.value = 0
        self.label['text'] = str(self.value)


def forget(kind, *a):
    """Очищает окно от выбранных виджетов"""
    if kind == 'Pack':
        for i in a:
            i.pack_forget()
    elif kind == 'Place':
        for i in a:
            i.place_forget()
    else:
        for i in a:
            i.grid_forget()



if __name__ == '__main__':
    MyApp = App()
    # События
    for i in MyApp.buttons: i.bind("<Button-1>", MyApp.push)
    MyApp.canvas.tag_bind(MyApp.reset_button, "<Button-1>", MyApp.reset)
    # Главный цикл
    MyApp.mainloop()