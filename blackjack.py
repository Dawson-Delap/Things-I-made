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
         '2♣': 'black',
         '3♣': 'black',
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
colnum = 0
numplay = 0
hidendeal = 0
stopper = 0
numdeal = 0
hidennum = 0
stop = 0
def hits(here):
    global numplay
    if here == 1:
        start.destroy()
        hit = Button(window, text="Hit", font=("Arial", 25), width=4, height=1, bg="gold", command=lambda: hits(0)).grid(row=2,column=0)
        pas = Button(window, text="pass", font=("Arial", 25), width=4, height=1, bg="gold", command=lambda: passs(0)).grid(row=2,column=2)
        hits(0)
    global cards
    global deal
    global play
    global colnum
    global stopper
    global numdeal
    global hidendeal
    global hidennum
    global stop
    deal = random.choice(list(cards.keys()))
    play = random.choice(list(cards.keys()))
    if stop <= 1:
        dealer["text"] = deal
        dealer["fg"] = colors[deal]
        numdeal = cards[deal]
        hidennum += cards[deal]
        stop += 1
    player["text"] = play
    dealer["fg"] = colors[deal]
    if stopper == 0:
        stopper = 1
        hidendeal = deal
        print(hidendeal)
    numplay += cards[play]
    dealnum["text"] = numdeal
    colnum += 1
    playnum["text"] = numplay
    cards.pop(deal)
    cards.pop(play)
    card = Button(window, text=play, fg=player['fg'], font=("Arial", 25), width=4, height=4).grid(row=3, column=colnum)
def passs(rev):
    hide["text"] = hidendeal
    dealnum["text"] = hidennum
window = Tk()
window.config(bg="darkgreen")
dealer = Button(window, text="dealer", font=("Arial", 25), width=8, height=8)
dealer.grid(row=0, column=1)
hide = Button(window, text="hidden", font=("Arial", 25), width=8, height=8)
hide.grid(row=0, column=0)
player = Button(window, text="player", font=("Arial", 25), width=8, height=8)
player.grid(row=1, column=1)
start = Button(window, text="Start", font=("Arial", 25), width=4, height=1, bg="gold",  command=lambda:  hits(1))
start.grid(row=2, column=1)
playnum = Button(window, text="0", font=("Arial", 25), bg="gold")
playnum.grid(row=3, column=0)
dealnum = Button(window, text="0", font=("Arial", 25), bg="gold")
dealnum.grid(row=0, column=2)
window.mainloop()