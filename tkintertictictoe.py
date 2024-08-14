from tkinter import *
xo =  "X"
x1 = 1
x2 = 2
x3 = 3
y1 = 4
y2 = 5
y3 = 6
z1 = 7
z2 = 8
z3 = 9
xlst = []
olst = []
win = 0
def work(button, place):
    global xo
    global x1 
    global x2 
    global x3 
    global y1 
    global y2 
    global y3 
    global z1 
    global z2 
    global z3 
    global xlst
    global olst
    global win
    row = button.grid_info()["row"]
    column = button.grid_info()["column"]
    button.destroy()
    new = Button(window, text=xo, height=16, width=16,).grid(row=row, column=column)
    if xo == "X":
        xlst.append(place)
        xo = "O"
    else:
        olst.append(place)
        xo = "X"
    
    if x1 in xlst and x2 in xlst and x3 in xlst:
        xo = "X"
        win = 1
    if y1 in xlst and y2 in xlst and y3 in xlst:
        xo = "X"
        win = 1
    if z1 in xlst and z2 in xlst and z3 in xlst:
        xo = "X"
        win = 1
    if x1 in xlst and y1 in xlst and z1 in xlst:
        xo = "X"
        win = 1
    if x2 in xlst and y2 in xlst and z2 in xlst:
        xo = "X"
        win = 1
    if x3 in xlst and y3 in xlst and z3 in xlst:
        xo = "X"
        win = 1
    if x1 in xlst and y2 in xlst and z3 in xlst:
        xo = "X"
        win = 1
    if x3 in xlst and y2 in xlst and z1 in xlst:
        xo = "X"
        win = 1
    
    
    if x1 in olst and x2 in olst and x3 in olst:
        xo = "O"
        win = 1
    if y1 in olst and y2 in olst and y3 in olst:
        xo = "O"
        win = 1
    if z1 in olst and z2 in olst and z3 in olst:
        xo = "O"
        win = 1
    if x1 in olst and y1 in olst and z1 in olst:
        xo = "O"
        win = 1
    if x2 in olst and y2 in olst and z2 in olst:
        xo = "O"
        win = 1
    if x3 in olst and y3 in olst and z3 in olst:
        xo = "O"
        win = 1
    if x1 in olst and y2 in olst and z3 in olst:
        xo = "O"
        win = 1
    if x3 in olst and y2 in olst and z1 in olst:
        xo = "O"
        win = 1
    if win == 1:
        win = Tk()
        lbl = Label(win, text= xo + " Wins!")
        lbl.pack()
        win.mainloop()
    
window = Tk()
a1 = Button(window, text="_", height=16, width=16, command=lambda: work(a1, x1))
a1.grid(row=0, column=0)
a2 = Button(window, text="_", height=16, width=16, command=lambda: work(a2, x2))
a2.grid(row=1, column=0)
a3 = Button(window, text="_", height=16, width=16, command=lambda: work(a3, x3))
a3.grid(row=2, column=0)
b1 = Button(window, text="_", height=16, width=16, command=lambda: work(b1, y1))
b1.grid(row=0, column=1)
b2 = Button(window, text="_", height=16, width=16, command=lambda: work(b2, y2))
b2.grid(row=1, column=1)
b3 = Button(window, text="_", height=16, width=16, command=lambda: work(b3, y3))
b3.grid(row=2, column=1)
c1 = Button(window, text="_", height=16, width=16, command=lambda: work(c1, z1))
c1.grid(row=0, column=2)
c2 = Button(window, text="_", height=16, width=16, command=lambda: work(c2, z2))
c2.grid(row=1, column=2)
c3 = Button(window, text="_", height=16, width=16, command=lambda: work(c3, z3))
c3.grid(row=2, column=2)
window.mainloop()
