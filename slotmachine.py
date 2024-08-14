from tkinter import *
import random
import emoji
ran = 0
rancolor = 0
moneynum = 0
def slots(Event=None):
    global moneynum
    moneynum -= 10
    rand()
    slot1["text"] = ran
    slot1["bg"] = rancolor
    rand()
    slot2["text"] = ran
    slot2["bg"] = rancolor
    rand()
    slot3["text"] = ran
    slot3["bg"] = rancolor
    if slot1["text"] == slot2["text"] and slot2["text"] == slot3["text"]:
        if slot1["text"] != 7:
            moneynum += 1000
        else:
            moneynum += 100000
    money["text"] = "Money: $", moneynum

def rand():
    global ran
    global rancolor
    opt = [emoji.emojize(':thumbs_up:'),emoji.emojize(':red_heart:'), emoji.emojize(':monkey:'), emoji.emojize(":orangutan:"), emoji.emojize(':four_leaf_clover:'), emoji.emojize(':cherries:'), emoji.emojize(":hot_dog:"), emoji.emojize(":hamburger:"), emoji.emojize(":chocolate_bar:"), 7]
    ran = random.choice(opt)
    colors = ["turquoise1", "yellow", "lawngreen", "blue", "hotpink"]
 
    rancolor = random.choice(colors)
        

window = Tk()
slot1 = Button(window, text=ran, font=("Arial", 25), height=16, width=16, bg="blue")
slot1.grid(row=0, column=0)
slot2 = Button(window, text=ran, font=("Arial", 25), height=16, width=16, bg="blue")
slot2.grid(row=0, column=1)
slot3 = Button(window, text=ran, font=("Arial", 25), height=16, width=16, bg="blue")
slot3.grid(row=0, column=2)
w = Button(window, height=16, font=("Arial", 25), width=3, bg="red")
w.grid(row = 0, column=3)
window.bind('<space>', slots)
money = Label(window, text=moneynum, font =("Arial", 10))
money.grid(row = 1, column=2)
window.mainloop()