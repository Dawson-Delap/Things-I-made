from tkinter import *
import random
import time

ran = 0
rancolor = 0
moneynum = 0

stopper = 1
qued = 0
rolls = 0
def querollcheck(): #update the text in the window with roll numbers
    global qued
    global rolls
    qued -= 1
    rolls += 1
    queued["text"] = "Queued = " + str(qued)
    roll["text"] = "Rolls = " + str(rolls)       
def slots(Event=None): #function that makes it roll
    global moneynum
    global qued
    global rolls
    moneynum -= 10
    qued += 1
    #update text in window with money and update queued rolls
    money["text"] = "Money: $ " + str(moneynum)
    queued["text"] = "Queued = " + str(qued)
    for i in range(0,10): #roll first slot
        rand()
        slot1["text"] = ran
        slot1["bg"] = rancolor
        window.update()
        time.sleep(.1)
    for i in range(0,10): #roll second slot
        rand()
        slot2["text"] = ran
        slot2["bg"] = rancolor
        window.update()
        time.sleep(.1)
    for i in range(0,10): #roll third slot
        rand()
        slot3["text"] = ran
        slot3["bg"] = rancolor
        window.update()
        time.sleep(.1)
    if slot1["text"] == slot2["text"] and slot2["text"] == slot3["text"]: #check if slots match
        if slot1["text"] != 7: #check if they are 7s
            moneynum += 1000
            last["text"] = "+$1000 on roll " + str(rolls+1) 
            money["text"] = "Money: $ " + str(moneynum)
        else:
            moneynum += 100000
            last["text"] = "+$100000 on roll " + str(rolls+1)
            money["text"] = "Money: $ " + str(moneynum)
    querollcheck()#update roll and que numbers

def rand(): #randomizer for the slots
    global ran
    global rancolor
    num = random.randint(0, 7)
    opt = ["\N{grinning face}", "\N{pancakes}", "\N{potato}", "\N{billiards}", "\N{slot machine}", "\N{rock}", "\N{page facing up}", "\N{black scissors}", 7]
    ran = opt[num]
    colors = ["turquoise1", "yellow", "lawngreen", "blue", "hotpink", "orange", "red", "purple"]
    rancolor = colors[num]
        

window = Tk() #open window
window.title("I LOVE GAMBLING!!!")
window.config(bg="darkgreen")
window.geometry("600x400")

for i in range(3):
    window.columnconfigure(i, weight=1)
for i in range(3):
    window.rowconfigure(i, weight=1)
#slots
slot1 = Button(window, text=ran, font=("Arial", 25), bg="blue")
slot1.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
slot2 = Button(window, text=ran, font=("Arial", 25), bg="blue")
slot2.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
slot3 = Button(window, text=ran, font=("Arial", 25), bg="blue")
slot3.grid(row=0, column=2, sticky="nsew", padx=10, pady=10)
#keybind for rolling
window.bind('<Return>', slots)
#bottom info
money = Label(window, text=moneynum, font =("Arial", 10))
money.grid(row = 1, column=1, sticky="nsew", padx=10, pady=10)
queued = Label(window, text="Queued = 0")
queued.grid(row=1, column=2, sticky="nsew", padx=10, pady=10)
roll = Label(window, text="Rolls = 0")
roll.grid(row=2, column=2, sticky="nsew", padx=10, pady=10)
last = Label(window, text="Last gain")
last.grid(row=2, column=1, sticky="nsew", padx=10, pady=10)
howto = Label(window, text="Enter to spin", font =("Arial", 7))
howto.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
window.mainloop() #keep window running
