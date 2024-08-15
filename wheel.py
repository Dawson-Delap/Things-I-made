from tkinter import *
import random
import time
opt = {
        "$1":1,
        "$10":10,
        "$100":100,
        "$1000":1000,
        "$10000":10000,
        "$100000":100000,
        "$1000000":1000000,
        "$10000000":10000000,
    }
moneys = 0
def work():
    global opt
    global moneys
    numran = random.randint(10,25)
    moneys -= 100000
    y = 0
    for i in range(0, numran):
        x = spot2["text"]
        y = spot1["text"]
        colors = spot2["bg"]
        ycolors = spot1["bg"]
        spot1["text"] = x
        spot1["bg"] = colors
        window.update()
        time.sleep(.01)
        colors = spot3["bg"]
        x = spot3["text"]
        spot2["text"] = x
        spot2["bg"] = colors
        window.update()
        time.sleep(.01)
        colors = spot4["bg"]
        x = spot4["text"]
        spot3["text"] = x
        spot3["bg"] = colors
        window.update()
        time.sleep(.01)
        colors = spot5["bg"]
        x = spot5["text"]
        spot4["text"] = x
        spot4["bg"] = colors
        window.update()
        time.sleep(.01)
        colors = spot6["bg"]
        x = spot6["text"]
        spot5["text"] = x
        spot5["bg"] = colors
        window.update()
        time.sleep(.01)
        colors = spot7["bg"]
        x = spot7["text"]
        spot6["text"] = x
        spot6["bg"] = colors
        window.update()
        time.sleep(.01)
        colors = spot8["bg"]
        x = spot8["text"]
        spot7["text"] = x
        spot7["bg"] = colors
        window.update()
        time.sleep(.01)

        spot8["text"] = y
        spot8["bg"] = ycolors
        window.update()
        time.sleep(.01)
    winmon = opt[spot6["text"]]
    moneys += winmon
    money["text"] = "Money: $" + str(moneys)
window = Tk()
spot1 =  Button(window, text = "$1", font=("Arial", 25), height=4, width=8, bg ="red")
spot1.grid(row=0, column=0)
spot2 =  Button(window, text = "$10", font=("Arial", 25), height=4, width=8, bg ="orange")
spot2.grid(row=0, column=1)
spot3 =  Button(window, text = "$100", font=("Arial", 25), height=4, width=8, bg ="gold")
spot3.grid(row=0, column=2)
spot4 =  Button(window, text = "$1000", font=("Arial", 25), height=4, width=8, bg ="yellow")
spot4.grid(row=1, column=2)
spot5 =  Button(window, text = "$10000", font=("Arial", 25), height=4, width=8, bg ="green")
spot5.grid(row=2, column=2)
spot6 =  Button(window, text = "$100000", font=("Arial", 25), height=4, width=8, bg ="aquamarine")
spot6.grid(row=2, column=1)
spot7 =  Button(window, text = "$1000000", font=("Arial", 25), height=4, width=8, bg="blue")
spot7.grid(row=2, column=0)
spot8 =  Button(window, text = "$10000000", font=("Arial", 25), height=4, width=8, bg="magenta")
spot8.grid(row=1, column=0)
middle = Button(window, text='''|
|
V''', font=("Arial", 25), height=4, width=8, bg ="orangered")
middle.grid(row=1, column=1)
spin = Button(window, text = "SPIN!!!", font=("Arial", 25), height=1, width=8, command=lambda: work())
spin.grid(row=3, column=1)
money = Label(window, text="Money: $"+ str(moneys))
money.grid(row=3, column=0)
price = Label(window, text= "100,000 per spin")
price.grid(row=3, column=2)
window.mainloop()

