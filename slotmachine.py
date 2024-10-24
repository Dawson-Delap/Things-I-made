from tkinter import *
import random
import emoji
import time
#if there is an error, type into cmd: 
# pip install emoji 
# pip install pyodbc

import pyodbc 
namelst = []
moneylst= []
try:
    cnxn = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};"
                        "Server=M-24955;"
                        "Database=slots;"
                        "UID=persons;"
                        "PWD=911")
    cursor = cnxn.cursor()
    cursor.execute('SELECT * FROM moneyown')
    for row in cursor:
        namelst.append(row[0])
        print(namelst)
        moneylst.append(row[1])
        print(moneylst)
except:
    def cont():
        nocon.destroy()
    nocon = Tk()
    nocon.config(bg="darkgreen")
    lbl = Label(nocon, text="No Sever Connection", font=("Arial", 50), bg="darkgreen", fg="gold")
    lbl.grid(row=0, column=0)
    but = Button(nocon, text="Continue", font=("Arial", 25), bg="gold", command=lambda: cont())
    but.grid(row=1, column=0)
    nocon.mainloop()
    offline = 1
    pass
def log():
    global moneynum
    inputname = nameinput.get()
    if inputname in namelst:
        sqlmoney = moneylst[namelst.index(inputname)]
        moneynum = sqlmoney
        money["text"] = "Money: $", moneynum
    else:
        pass



ran = 0
rancolor = 0
moneynum = 0

stopper = 1
qued = 0
rolls = 0
def save():
            global qued
            global rolls
            qued -= 1
            rolls += 1
            queued["text"] = "Queued = " + str(qued)
            roll["text"] = "Rolls = " + str(rolls)
            savename = nameinput.get()
            if nameinput.get() not in namelst:
                cursor.execute(f"INSERT INTO moneyown VALUES ('{savename}', {moneynum})")
                cursor.commit()
            else:
                cursor.execute(f"update moneyown set money = {moneynum} where name = '{savename}'")
                cursor.commit()
            
def deletesave():
    savename = nameinput.get()
    cursor.execute(f"delete from moneyown where name = '{savename}'")
    cursor.commit()
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
            last["text"] = "+$1000 image match on roll " + str(rolls+1) 
        else:
            moneynum += 100000
            last["text"] = "+$100000 all 7s on roll " + str(rolls+1)
    if slot1["bg"] == slot2["bg"] and slot2["bg"] == slot3["bg"]:
         moneynum += 500
         last["text"] = "+$500 color match on roll " + str(rolls+1)
    money["text"] = "Money: $ "+ str(moneynum)
    queued["text"] = "Queued = "+ str(qued)
    save()

def rand():
    global ran
    global rancolor
    opt = [emoji.emojize(':thumbs_up:'), emoji.emojize(':monkey:'), emoji.emojize(":orangutan:"), emoji.emojize(':four_leaf_clover:'), emoji.emojize(':cherries:'), emoji.emojize(":hot_dog:"), emoji.emojize(":hamburger:"), emoji.emojize(":chocolate_bar:"), 7]
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
if offline == 0:
    nameinput = Entry(window)
    nameinput.grid(row=3, column=1)
    login = Button(window, text="Log in", command= lambda: log())
    login.grid(row=4, column=1)
    savebut = Button(window, text="Save", command= lambda: save())
    savebut.grid(row=5, column=1)
    deletebut = Button(window, text="Delete Save", command= lambda: deletesave())
    deletebut.grid(row=6,column=1)
window.mainloop()
