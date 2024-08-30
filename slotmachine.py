from tkinter import *
import random
import emoji
import time
#if there is an error, type into cmd: pip install emoji 
ran = 0
rancolor = 0
moneynum = 0
def slots(Event=None):
    global moneynum
    moneynum -= 10
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
window.bind('<space>', slots)
window.bind('<z>', slots)
window.bind('<x>', slots)
money = Label(window, text=moneynum, font =("Arial", 10))
money.grid(row = 1, column=1)
howto = Label(window, text="Space to spin", font =("Arial", 7))
howto.grid(row=1, column=0)
window.mainloop()