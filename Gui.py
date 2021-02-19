from tkinter import *
root = Tk()
root.wm_state("zoomed")
w, h = root.winfo_screenwidth() * 4/5, root.winfo_screenheight()
canvas = Canvas(root, width=w, height=h)
canvas.place(relx=0, rely=0)
oval1 = canvas.create_oval(0, 0, 100, 100, fill='red')
oval2 = canvas.create_oval(100, 100, 200, 200, fill='black')
rec = canvas.create_rectangle(200, 200, 300, 300, fill="blue")


class twocubes(Canvas):
    def __init__(self,  width, height, x, y):
        self.width=width
        self.height = height
        self.Rec = canvas.create_rectangle(x, y, x+width, y + height, fill="red")
        self.Rec2 = canvas.create_rectangle(x, y+height, x+width, y + 2 *height, fill="red")
        self.x = x
        self.y = y
    def bind(self):
        canvas.tag_bind(self.Rec, '<B1-Motion>', lambda event: move2(event, self.Rec))
        canvas.tag_bind(self.Rec2, '<B1-Motion>', lambda event: move2(event, self.Rec2))
    def coords(self, x1=None, y1=None):
        if x1 != None:
            canvas.coords(self.Rec, x1, y1, x1 + self.width, y1+self.height)
            canvas.coords(self.Rec2, x1, y1+ self.height, x1 + self.width, y1 + 2 * self.height)
            self.x = x1
            self.y = y1
        else:
            return [self.x, self.y]


        
        
b = twocubes(50, 50, 300, 300)

def move(event, shape):
    canvas.coords(shape, 
        event.x + (canvas.coords(shape)[2] - canvas.coords(shape)[0])/2,
        event.y + (canvas.coords(shape)[3] - canvas.coords(shape)[1])/2,
        event.x - (canvas.coords(shape)[2] - canvas.coords(shape)[0])/2,
        event.y - (canvas.coords(shape)[3] - canvas.coords(shape)[1])/2
    )

def move2(event, shape):
    b.coords( 
        event.x,
        event.y,
    )



a = [oval1, oval2, rec]
for i in a:
    eval("canvas.tag_bind({}, '<B1-Motion>', lambda event: move(event, {}))".format(i, i))
b.bind()
root.mainloop()