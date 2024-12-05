from tkinter import *
import random
import time

ran = 0
rancolor = 0
moneynum = 0

stopper = 1
qued = 0
rolls = 0
def querollcheck():
            global qued
            global rolls
            qued -= 1
            rolls += 1
            queued["text"] = "Queued = " + str(qued)
            roll["text"] = "Rolls = " + str(rolls)       
def slots(Event=None):
    global moneynum
    global qued
    global rolls
    moneynum -= 10
    qued += 1
    money["text"] = "Money: $ " + str(moneynum)
    queued["text"] = "Queued = " + str(qued)
    for i in range(0,10):
        rand()
        slot1["text"] = ran
        slot1["bg"] = rancolor
        window.update()
        time.sleep(.1)
    for i in range(0,10):
        rand()
        slot2["text"] = ran
        slot2["bg"] = rancolor
        window.update()
        time.sleep(.1)
    for i in range(0,10):
        rand()
        slot3["text"] = ran
        slot3["bg"] = rancolor
        window.update()
        time.sleep(.1)
    if slot1["text"] == slot2["text"] and slot2["text"] == slot3["text"]:
        if slot1["text"] != 7:
            moneynum += 1000
            last["text"] = "+$1000 on roll " + str(rolls+1) 
            money["text"] = "Money: $ " + str(moneynum)
        else:
            moneynum += 100000
            last["text"] = "+$100000 on roll " + str(rolls+1)
            money["text"] = "Money: $ " + str(moneynum)
    querollcheck()

def rand():
    global ran
    global rancolor
    opt = ["\N{grinning face}", "\N{pancakes}", "\N{potato}", "\N{billiards}", "\N{slot machine}", "\N{rock}", "\N{page facing up}", "\N{black scissors}", 7]
    ran = random.choice(opt)
    colors = ["turquoise1", "yellow", "lawngreen", "blue", "hotpink"]
    rancolor = random.choice(colors)
        

window = Tk()
window.config(bg="darkgreen")
slot1 = Button(window, text=ran, font=("Arial", 25), height=8, width=8, bg="blue")
slot1.grid(row=0, column=0)
slot2 = Button(window, text=ran, font=("Arial", 25), height=8, width=8, bg="blue")
slot2.grid(row=0, column=1)
slot3 = Button(window, text=ran, font=("Arial", 25), height=8, width=8, bg="blue")
slot3.grid(row=0, column=2)
window.bind('<Return>', slots)
money = Label(window, text=moneynum, font =("Arial", 10))
money.grid(row = 1, column=1)
queued = Label(window, text="Queued = 0")
queued.grid(row=1, column=2)
roll = Label(window, text="Rolls = 0")
roll.grid(row=2, column=2)
last = Label(window, text="Last gain")
last.grid(row=2, column=1)
howto = Label(window, text="Enter/Return to spin", font =("Arial", 7))
howto.grid(row=1, column=0)
window.mainloop()
