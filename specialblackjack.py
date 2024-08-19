from tkinter import *
import random

cards = {
        #clubs
         '2♣':2,
         '3♣':3,
         '4♣':4,
         '5♣':5,
         '6♣':6,
         '7♣':7,
         '8♣':8,
         '9♣':9,
         '10♣':10,
         'J♣':10,
         'Q♣':10,
         'K♣':10,
         'A♣':11,
        #spades
         '2♠':2,
         '3♠': 3,
         '4♠': 4,
         '5♠': 5,
         '6♠': 6,
         '7♠': 7,
         '8♠': 8,
         '9♠': 9,
         '10♠': 10,
         'J♠': 10,
         'Q♠': 10,
         'K♠': 10,
         'A♠': 11,
        #diamonds
         '2♦': 2,
         '3♦': 3,
         '4♦': 4,
         '5♦': 5,
         '6♦': 6,
         '7♦': 7,
         '8♦': 8,
         '9♦': 9,
         '10♦': 10,
         'J♦': 10,
         'Q♦': 10,
         'K♦': 10,
         'A♦': 11,
        #hearts
         '2♥': 2,
         '3♥': 3,
         '4♥': 4,
         '5♥': 5,
         '6♥': 6,
         '7♥': 7,
         '8♥': 8,
         '9♥': 9,
         '10♥': 10,
         'J♥': 10,
         'Q♥': 10,
         'K♥': 10,
         'A♥': 11,
        }  
colors = {
        #clubs
         '2♣':'black',
         '3♣':'black',
         '4♣':'black',
         '5♣':'black',
         '6♣':'black',
         '7♣':'black',
         '8♣':'black',
         '9♣':'black',
         '10♣':'black',
         'J♣':'black',
         'Q♣':'black',
         'K♣':'black',
         'A♣':'black',
        #spades
         '2♠':'black',
         '3♠': 'black',
         '4♠': 'black',
         '5♠': 'black',
         '6♠': 'black',
         '7♠': 'black',
         '8♠': 'black',
         '9♠': 'black',
         '10♠':'black',
         'J♠': 'black',
         'Q♠': 'black',
         'K♠': 'black',
         'A♠': 'black',
        #diamonds
         '2♦': 'red',
         '3♦': 'red',
         '4♦': 'red',
         '5♦': 'red',
         '6♦': 'red',
         '7♦': 'red',
         '8♦': 'red',
         '9♦': 'red',
         '10♦': 'red',
         'J♦': 'red',
         'Q♦': 'red',
         'K♦': 'red',
         'A♦': 'red',
        #hearts,
         '2♥': 'red',
         '3♥': 'red',
         '4♥': 'red',
         '5♥': 'red',
         '6♥': 'red',
         '7♥': 'red',
         '8♥': 'red',
         '9♥': 'red',
         '10♥': 'red',
         'J♥': 'red',
         'Q♥': 'red',
         'K♥': 'red',
         'A♥': 'red',
        } 
deal = 0
play = 0
colnum = 3
numplay = 0
hidendeal = 0
stopper = 0
numdeal = 0
hidennum = 0
stop = 0
dealcol = 3
winer = 0
loser = 0
def hits(here):
    global numplay
    global cards
    global deal
    global play
    global colnum
    global stopper
    global numdeal
    global hidendeal
    global hidennum
    global stop
    if here == 1:
        start.destroy()
        hit = Button(window, text="Hit", font=("Arial", 25), width=4, height=1, bg="gold", command=lambda: hits(0)).grid(row=2,column=0)
        pas = Button(window, text="pass", font=("Arial", 25), width=4, height=1, bg="gold", command=lambda: passs(0)).grid(row=2,column=2)
        deal = random.choice(list(cards.keys()))
        hidendeal = random.choice(list(cards.keys()))
        dealer["text"] = deal
        dealer["fg"] = colors[deal]
        numdeal = cards[deal]
        print(hidendeal)
        dealnum["text"] = numdeal
        cards.pop(deal)
        win()
    print("runs")
    play = random.choice(list(cards.keys()))
    play2 = random.choice(list(cards.keys()))
    player["text"] = play
    player["fg"] = colors[deal]
    numplay += cards[play]
    numplay += cards[play2]
    playnum["text"] = numplay
    cards.pop(play)
    cards.pop(play2)
    card = Button(window, text=play2, fg=colors[play2], font=("Arial", 25), width=8, height=8).grid(row=1, column=2)
    win()
    if here == 0:
        another()
def passs(rev):
    global numdeal
    global dealcol
    global stop
    hide["text"] = hidendeal
    hide["fg"] = colors[hidendeal]
    if stop == 0:
        numdeal += cards[hidendeal]
        dealnum["text"] = numdeal
        stop = 1
    dealnum["text"] = numdeal
    deal2 = random.choice(list(cards.keys()))
    deal2num = cards[deal2]
    cards.pop(deal2)
    numdeal += deal2num
    dealnum["text"] = numdeal
    card = Button(window, text=deal2, fg=colors[deal2], font=("Arial", 25), width=4, height=4).grid(row=0, column=dealcol)
    dealcol += 1
    win()
    passwin()
def another():
    global colnum
    another1 = random.choice(list(cards.keys()))
    cards.pop(another1)
    card = Button(window, text=another1, fg=colors[another1], font=("Arial", 25), width=4, height=4).grid(row=1, column=colnum)
    colnum += 1
    win()
def win():
    global loser
    global winer
    if numplay > 21:
        loser = 1
    if numdeal > 21:
        winer = 1
    if loser == 1:
        lose = Tk()
        l = Label(lose, text= "YOU LOST YOUR KIDS AND WIFE", font=("Arial", 75))
        l.pack()
        lose.mainloop()
    if winer == 1:
        wine = Tk()
        w = Label(wine, text= "YOU WON :)", font=("Arial", 100))
        w.pack()
        wine.mainloop()
def passwin():
    if numdeal > numplay:
        lose = Tk()
        l = Label(lose, text= "YOU LOST YOUR KIDS AND WIFE", font=("Arial", 75))
        l.pack()
        lose.mainloop()
    if numplay > numdeal:
        wine = Tk()
        w = Label(wine, text= "YOU WON :)", font=("Arial", 100))
        w.pack()
        wine.mainloop()
window = Tk()
window.config(bg="darkgreen")
dealer = Button(window, text="dealer", font=("Arial", 25), width=8, height=8)
dealer.grid(row=0, column=1)
hide = Button(window, text="hidden", font=("Arial", 25), width=8, height=8)
hide.grid(row=0, column=2)
player = Button(window, text="player", font=("Arial", 25), width=8, height=8)
player.grid(row=1, column=1)
start = Button(window, text="Start", font=("Arial", 25), width=4, height=1, bg="gold",  command=lambda:  hits(1))
start.grid(row=2, column=1)
playnum = Button(window, text="0", font=("Arial", 25), bg="gold")
playnum.grid(row=1, column=0)
dealnum = Button(window, text="0", font=("Arial", 25), bg="gold")
dealnum.grid(row=0, column=0)
window.mainloop()