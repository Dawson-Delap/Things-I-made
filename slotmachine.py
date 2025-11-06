from tkinter import *
import random
import time
import json
import os

ran = 0
rancolor = 0
moneynum = 0
qued = 0
rolls = 0
gains = ""
def save_data():
    data = {
        "moneynum": moneynum,
        "rolls": rolls,
        "gains" : gains
    }
    with open("save.json", "w") as file:
        json.dump(data, file)

def load_data():
    global moneynum, rolls, qued, money, roll, gains
    if os.path.exists("save.json"):
        with open("save.json", "r") as file:
            data = json.load(file)
            moneynum = data.get("moneynum", 0)
            rolls = data.get("rolls", 0) 
            gains = data.get("gains", "")

def querollcheck(): #update the text in the window with roll numbers
    global qued,rolls, moneynum
    qued -= 1
    moneynum -= 10
    rolls += 1
    queued["text"] = "Queued = " + str(qued)
    roll["text"] = "Rolls = " + str(rolls)  
    money["text"] = "Money: $ " + str(moneynum)     
def slots(Event=None): #function that makes it roll
    global moneynum
    global qued
    global rolls
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
            add_last_gain("+$1000 on roll " + str(rolls+1))
            money["text"] = "Money: $ " + str(moneynum)
        else:
            moneynum += 100000
            add_last_gain("+$100000 on roll " + str(rolls+1))
            money["text"] = "Money: $ " + str(moneynum)
    querollcheck()#update roll and que numbers

def rand(): #randomizer for the slots
    global ran
    global rancolor
    num = random.randint(0, 8)
    opt = ["\N{grinning face}", "\N{pancakes}", "\N{potato}", "\N{billiards}", "\N{slot machine}", "\N{rock}", "\N{page facing up}", "\N{black scissors}", 7]
    ran = opt[num]
    colors = ["turquoise1", "orchid", "lawngreen", "blue", "hotpink", "orange", "red", "purple", "gold"]
    rancolor = colors[num]

def add_last_gain(text): #add text to last gain
    global gains
    gains = gains + text +"\n"
    gainstext["text"] = gains
    canvas.configure(scrollregion=canvas.bbox("all"))      

window = Tk() #open window
window.title("I LOVE GAMBLING!!!")
window.config(bg="darkgreen")
window.geometry("600x400")
load_data()
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

# Create a frame to hold the scrollable content
scroll_frame = Frame(window)
scroll_frame.grid(row=2, column=1, sticky="nsew", padx=10, pady=10)

# Create a canvas inside the frame
canvas = Canvas(scroll_frame, width=150, height=100)
canvas.pack(side=LEFT, fill=BOTH, expand=True)

# Add scrollbar to the canvas
scrollbar = Scrollbar(scroll_frame, orient=VERTICAL, command=canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)

canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

# Frame inside canvas to hold labels
scrollable_content = Frame(canvas)
canvas.create_window((0, 0), window=scrollable_content, anchor="nw")
gainstext = Label(scrollable_content, text="Gains will show here")
gainstext.pack()
howto = Label(window, text="Enter to spin", font =("Arial", 10))
howto.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
money["text"] = "Money: $ " + str(moneynum)
roll["text"] = "Rolls = " + str(rolls)
gainstext["text"] = gains
def on_close():
    save_data()
    window.destroy()
window.protocol("WM_DELETE_WINDOW", on_close)
window.mainloop() #keep window running
