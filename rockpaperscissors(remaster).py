from tkinter import *
import random
opt = ["Rock", "Paper", "Rock", "Paper", "Scissors", "Rock", "Paper", "Scissors"]
def botwork():
    global opt
    global botchoose
    global botwindow
    global botstop
    window.destroy()
    botchoose = random.choice(opt)
    botwindow = Tk()
    botwindow.config(bg="darkgreen")
    rock = Button(botwindow, text="Rock", height=2, width=7, font=("arial", 25), bg="gold",  command= lambda: botplay("Rock"), )
    rock.grid(row=1, column=0)
    paper = Button(botwindow, text = "Paper", height=2, width=7, font=("arial", 25), bg="gold", command= lambda: botplay("Paper"))
    paper.grid(row=1, column=1)
    scissors = Button(botwindow, text="Scissors", height=2, width=7, font=("arial", 25), bg="gold", command= lambda: botplay("Scissors"))
    scissors.grid(row=1, column=2)
    botstop = 0
def botplay(playerchoose):
    global botwindow
    global botstop
    if playerchoose == "Paper" and botchoose == "Rock" and botstop == 0:
        winfun("Player Wins! Bot choose Rock")
    elif playerchoose == "Rock" and botchoose == "Scissors" and botstop == 0:
        winfun("Player Wins! Bot choose Scissors")
    elif playerchoose == "Scissors" and botchoose == "Paper" and botstop == 0:
        winfun("Player Wins! Bot choose Paper")
    elif playerchoose == botchoose and botstop == 0:
        winfun("Tie!")
    elif botstop == 0:
        winfun("Bot Wins ;(")
def winfun(wintext):
    lbl = Label(botwindow, text=wintext, font=("arial", 25))
    lbl.grid(row=2, column=1)
    restart = Button(botwindow, text="Restart?", font=("arial", 25), command=lambda:botrst())
    restart.grid(row=3, column=1)
    botstop = 1
def botrst():
    botwindow.destroy()
    mainwin()

def twowork():
    global opt
    global twowindow
    global play1ready
    global play2ready
    global onewindow
    global twowindow
    global stop2
    stop2 = 0
    window.destroy()

    onewindow = Tk()
    onewindow.config(bg="red")
    playone = Label(onewindow, text="Player 1", font=("arial", 25), bg="red")
    playone.grid(row=0, column=1)
    rock = Button(onewindow, text="Rock", height=2, width=7, font=("arial", 25), bg="red", command= lambda: play1("Rock"))
    rock.grid(row=1, column=0)
    paper = Button(onewindow, text = "Paper", height=2, width=7, font=("arial", 25), bg="red", command= lambda: play1("Paper"))
    paper.grid(row=1, column=1)
    scissors = Button(onewindow, text="Scissors", height=2, width=7, font=("arial", 25), bg="red", command= lambda: play1("Scissors"))
    scissors.grid(row=1, column=2)

    twowindow = Tk()
    twowindow.config(bg="blue")
    playtwo = Label(twowindow, text="Player 2", font=("arial", 25), bg="blue")
    playtwo.grid(row=0, column=1)
    rock = Button(twowindow, text="Rock", height=2, width=7, font=("arial", 25), bg="blue", command= lambda: play2("Rock"))
    rock.grid(row=1, column=0)
    paper = Button(twowindow, text = "Paper", height=2, width=7, font=("arial", 25), bg="blue", command= lambda: play2("Paper"))
    paper.grid(row=1, column=1)
    scissors = Button(twowindow, text="Scissors", height=2, width=7, font=("arial", 25), bg="blue", command= lambda: play2("Scissors"))
    scissors.grid(row=1, column=2)
    play1ready=0
    play2ready=0
    stop2 = 0
def play1(play1choose):
    global play1ready
    global chooseplay1
    play1ready = 1
    chooseplay1 = play1choose
    if play2ready == 1:
        play3()
def play2(play2choose):
    global play2ready
    global chooseplay2
    play2ready = 1
    chooseplay2 = play2choose
    if play1ready == 1:
        play3()

def play3():
    global win2
    global stop2
    if chooseplay1 == "Rock" and chooseplay2 == "Scissors" and stop2 == 0:
        win2fun("Player 1 Wins!")
    elif chooseplay1 == "Paper" and chooseplay2 == "Rock" and stop2 == 0:
        win2fun("Player 1 Wins!")
    elif chooseplay1 == "Scissors" and chooseplay2 == "Paper" and stop2 == 0:
        win2fun("Player 1 Wins!")
    elif chooseplay1 == chooseplay2 and stop2 == 0:
        win2fun("Tie!!")
    elif stop2 == 0:
        win2fun("Player 2 Wins!")
def win2fun(text2):
    global stop2
    global win2
    win2 = Tk()
    lbl = Label(win2, text=text2, font=("arial", 25))
    lbl.grid(row=2, column=1)
    restart = Button(win2, text="Restart?", font=("arial", 25), command=lambda: rst2())
    restart.grid(row=3, column=1)
    stop2 = 1
    win2.mainloop()
def rst2():
    win2.destroy()
    onewindow.destroy()
    twowindow.destroy()
    mainwin()
def mainwin():
    global window
    window = Tk()
    which = Label(window, text="What do you want to play?", font=("arial", 25))
    which.grid(row=0, column=1)
    twoplay = Button(window, text="2 Player", font=("arial", 25), command= lambda: twowork())
    twoplay.grid(row=1, column=0)
    botopt = Button(window, text="Bot", font=("arial", 25), command= lambda: botwork())
    botopt.grid(row=1, column=2)
    window.mainloop()
mainwin()