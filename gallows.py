#Игра виселица
from Gui import *

class Letter(Label):
    def __init__(self, master, width, height, letter=None, font_size=10):
        super().__init__(master, width=width, height=height, font=f"Tahoma {font_size}")
        self.letter = letter

    def show(self):
        self['text'] = self.letter


class Counter(Label):
    def __init__(self, master, font_size, name):
        super().__init__(master, font=f"Tahoma {font_size}")
        self.name = name



if __name__ == '__main__':

    a = Letter(root, 1, 1, 'A', 30)
    # a.pack()
    a.show()

    word = [i for i in "Ахмад".lower()]
    letters = []
    word_frame = Frame(root)
    for i in word:
        letters.append(Letter(word_frame, 1, 1, i, 40))
    
    for i in range(len(letters)):
       letters[i].grid(row=0, column=i)
       letters[i].show()
    word_frame.pack()
    print(word)

    print(root.winfo_screenwidth())
    print()

    root.mainloop()