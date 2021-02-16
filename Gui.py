from tkinter import *
root = Tk()
root.wm_state("zoomed")
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
canvas = Canvas(root, width=w, height=h)
canvas.pack()
oval1 = canvas.create_oval(0, 0, 100, 100, fill='red')
oval2 = canvas.create_oval(100, 100, 200, 200, fill='black')
rec = canvas.create_rectangle(200, 200, 300, 300, fill="blue")
print(canvas.coords(oval1))
def move(event, shape):
    canvas.coords(shape, 
        event.x + (canvas.coords(shape)[2] - canvas.coords(shape)[0])/2,
        event.y + (canvas.coords(shape)[3] - canvas.coords(shape)[1])/2,
        event.x - (canvas.coords(shape)[2] - canvas.coords(shape)[0])/2,
        event.y - (canvas.coords(shape)[3] - canvas.coords(shape)[1])/2
    )

a = [oval1, oval2, rec]
for i in a:
    eval("canvas.tag_bind({}, '<B1-Motion>', lambda event: move(event, {}))".format(i, i))

root.mainloop()