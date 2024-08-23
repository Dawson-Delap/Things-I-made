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
         'J♣':11,
         'Q♣':12,
         'K♣':13,
         'A♣':14,
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
         'J♠': 11,
         'Q♠': 12,
         'K♠': 13,
         'A♠': 14,
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
         'J♦': 11,
         'Q♦': 12,
         'K♦': 13,
         'A♦': 14,
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
         'J♥': 11,
         'Q♥': 12,
         'K♥': 13,
         'A♥': 14,
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
playnum = 0
botnum = 0
stop = 0
def start():
    window.destroy()
    lose.destroy()
    global playnum
    global botnum
    global stop
    global cards
    global colors
    playnum = 0
    botnum = 0
    stop = 0
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
            'J♣':11,
            'Q♣':12,
            'K♣':13,
            'A♣':14,
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
            'J♠': 11,
            'Q♠': 12,
            'K♠': 13,
            'A♠': 14,
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
            'J♦': 11,
            'Q♦': 12,
            'K♦': 13,
            'A♦': 14,
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
            'J♥': 11,
            'Q♥': 12,
            'K♥': 13,
            'A♥': 14,
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
    windows()
    deal()

def deal(Event=None):
    global lose 
    global stop
    if len(cards) != 0:
        botdeal()
        playdeal()
        award()
    else:
        if botnum > playnum and stop == 0:  
            stop = 1 
            lose = Tk()
            lose.config(bg="darkgreen")
            wol = Label(lose, text="YOU LOSE!", font=("Arial", 75), bg="darkgreen", fg="white")
            wol.grid(row=0, column=0)
            restart = Button(lose, text="Restart?", font=("Arial", 25), bg="gold", command=lambda: start())
            restart.grid(row=1, column=0)
            lose.mainloop()
        elif playnum > botnum and stop == 0: 
            stop = 1 
            lose = Tk()
            lose.config(bg="darkgreen")
            wol = Label(lose, text="YOU WIN!", font=("Arial", 75), bg="darkgreen", fg="white")
            wol.grid(row=0, column=0)
            restart = Button(lose, text="Restart?", font=("Arial", 25), bg="gold", command=lambda: start())
            restart.grid(row=1, column=0)
            lose.mainloop()
        elif stop == 0:
            stop = 1
            lose = Tk()
            lose.config(bg="darkgreen")
            wol = Label(lose, text="TIED!", font=("Arial", 75), bg="darkgreen", fg="white")
            wol.grid(row=0, column=0)
            restart = Button(lose, text="Restart?", font=("Arial", 25), bg="gold", command=lambda: start())
            restart.grid(row=1, column=0)
            lose.mainloop() 
def botdeal():
    global botcard
    global botnum
    global botcardnum
    global playcardnum
    if len(cards) !=0:
        botcard = random.choice(list(cards.keys()))
        botcardnum = cards[botcard]
        bot["text"] = botcard
        bot["fg"] = colors[botcard]
        cards.pop(botcard)
def playdeal():
    global playcard
    global playnum
    global playcardnum
    global botcardnum
    if len(cards) !=0:
        playcard = random.choice(list(cards.keys()))
        playcardnum = cards[playcard]
        player["text"] = playcard
        player["fg"] = colors[playcard]
        cards.pop(playcard)
def award():
    global botnum
    global playnum
    if  playcardnum > botcardnum:
            playnum += 1
            playnumbut["text"] = playnum
    if  botcardnum > playcardnum:
            botnum +=1
            botnumbut["text"] = botnum



def windows():
    global botnumbut
    global playnumbut
    global player
    global bot
    global window
    window = Tk()
    window.config(bg="darkgreen")
    bot = Button(window, text="bot", font=("Arial", 25), height=8, width=9)
    bot.grid(row=0, column=1)
    player = Button(window, text="player", font=("Arial", 25), height=8, width=9,)
    player.grid(row=1, column=1)
    botnumbut = Button(window, text=botnum, font=("Arial", 25), bg="gold")
    botnumbut.grid(row=0, column=0)
    playnumbut = Button(window, text=playnum, font=("Arial", 25), bg="gold")
    playnumbut.grid(row=1, column=0)
    startbut = Button(window, text="deal", font=("Arial", 25), bg="gold", command=lambda: deal())
    startbut.grid(row=2, column=1)
    window.bind('<space>', deal)
    window.mainloop()
windows()