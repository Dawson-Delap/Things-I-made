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
tie = 0
stoper = 0
def restart():
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
    global tie
    global stoper
    global winorlose
    window.destroy()
    winorlose.destroy()
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
    tie = 0
    stoper = 0
    wind()

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
    global stoper
    global tie
    row = button.grid_info()["row"]
    column = button.grid_info()["column"]
    button.destroy()
    if xo == "X":
        color = "red"
    elif xo == "O":
        color = "blue"
    new = Button(window, text=xo, height=4, width=4, font=("arial", 25), bg=color).grid(row=row, column=column)
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
    if len(xlst) == 5 and len(olst) == 4:
        tie = 1 
    if win == 1:
        if stoper == 0:
            stoper = 1
            global winorlose
            winorlose = Tk()
            winorlose.config(bg="darkorchid1")
            lbl = Label(winorlose, text= xo + " Wins!", font=("arial", 25), bg="darkorchid1")
            lbl.grid(row=0, column=0)
            res = Button(winorlose, text="Restart?", bg=color, command= lambda: restart())
            res.grid(row=1, column=0)
            winorlose.mainloop()
    if tie == 1:
        if stoper == 0:
                    stoper = 1
                    winorlose = Tk()
                    winorlose.config(bg="darkorchid1")
                    lbl = Label(winorlose, text="Tie!", font=("arial", 25), bg="darkorchid1")
                    lbl.grid(row=0, column=0)
                    res = Button(winorlose, text="Restart?", bg=color, command= lambda: restart())
                    res.grid(row=1, column=0)
                    winorlose.mainloop()


def wind():
    global window
    window = Tk()
    window.config(bg="darkorchid1")
    a1 = Button(window, text="_", height=4, width=4, command=lambda: work(a1, x1), font=("arial", 25), bg="darkorchid1")
    a1.grid(row=0, column=0)
    a2 = Button(window, text="_", height=4, width=4, command=lambda: work(a2, x2), font=("arial", 25), bg="darkorchid1")
    a2.grid(row=1, column=0)
    a3 = Button(window, text="_", height=4, width=4, command=lambda: work(a3, x3), font=("arial", 25), bg="darkorchid1")
    a3.grid(row=2, column=0)
    b1 = Button(window, text="_", height=4, width=4, command=lambda: work(b1, y1), font=("arial", 25), bg="darkorchid1")
    b1.grid(row=0, column=1)
    b2 = Button(window, text="_", height=4, width=4, command=lambda: work(b2, y2), font=("arial", 25), bg="darkorchid1")
    b2.grid(row=1, column=1)
    b3 = Button(window, text="_", height=4, width=4, command=lambda: work(b3, y3), font=("arial", 25), bg="darkorchid1")
    b3.grid(row=2, column=1)
    c1 = Button(window, text="_", height=4, width=4, command=lambda: work(c1, z1), font=("arial", 25), bg="darkorchid1")
    c1.grid(row=0, column=2)
    c2 = Button(window, text="_", height=4, width=4, command=lambda: work(c2, z2), font=("arial", 25), bg="darkorchid1")
    c2.grid(row=1, column=2)
    c3 = Button(window, text="_", height=4, width=4, command=lambda: work(c3, z3), font=("arial", 25), bg="darkorchid1")
    c3.grid(row=2, column=2)
    window.mainloop()
wind()
