from tkinter import *
import random
opt = ["Rock", "Paper", "Rock", "Paper", "Scissors", "Rock", "Paper", "Scissors"]
def botwork():
    global opt
    global botchoose
    global botwindow
    window.destroy()
    botchoose = random.choice(opt)
    botwindow = Tk()
    rock = Button(botwindow, text="Rock", height=2, width=7, font=("arial", 25), command= lambda: botplay("Rock"))
    rock.grid(row=1, column=0)
    paper = Button(botwindow, text = "Paper", height=2, width=7, font=("arial", 25), command= lambda: botplay("Paper"))
    paper.grid(row=1, column=1)
    scissors = Button(botwindow, text="Scissors", height=2, width=7, font=("arial", 25), command= lambda: botplay("Scissors"))
    scissors.grid(row=1, column=2)
def botplay(playerchoose):
    global botwindow
    if playerchoose == "Paper" and botchoose == "Rock":
        lbl = Label(botwindow, text="Player Wins! Bot choose Rock", font=("arial", 25))
        lbl.grid(row=2, column=1)
    elif playerchoose == "Rock" and botchoose == "Scissors":
        lbl = Label(botwindow, text="Player Wins! Bot choose Scissors", font=("arial", 25))
        lbl.grid(row=2, column=1)
    elif playerchoose == "Scissors" and botchoose == "Paper":
        lbl = Label(botwindow, text="Player Wins! Bot choose Paper", font=("arial", 25))
        lbl.grid(row=2, column=1)
    elif playerchoose == botchoose:
        lbl = Label(botwindow, text="Tie!", font=("arial", 25))
        lbl.grid(row=2, column=1)
    else:
        lbl = Label(botwindow, text="Bot Wins ;(", font=("arial", 25))
        lbl.grid(row=2, column=1)


def twowork():
    global opt
    window.destroy()
    onewindow = Tk()
    playone = Label(onewindow, text="Player 1", font=("arial", 25))
    playone.grid(row=0, column=1)
    rock = Button(onewindow, text="Rock", height=2, width=7, font=("arial", 25), command= lambda: play1("Rock"))
    rock.grid(row=1, column=0)
    paper = Button(onewindow, text = "Paper", height=2, width=7, font=("arial", 25), command= lambda: play1("Paper"))
    paper.grid(row=1, column=1)
    scissors = Button(onewindow, text="Scissors", height=2, width=7, font=("arial", 25), command= lambda: play1("Scissors"))
    scissors.grid(row=1, column=2)

    twowindow = Tk()
    playtwo = Label(twowindow, text="Player 2", font=("arial", 25))
    playtwo.grid(row=0, column=1)
    rock = Button(twowindow, text="Rock", height=2, width=7, font=("arial", 25), command= lambda: play2("Rock"))
    rock.grid(row=1, column=0)
    paper = Button(twowindow, text = "Paper", height=2, width=7, font=("arial", 25), command= lambda: play2("Paper"))
    paper.grid(row=1, column=1)
    scissors = Button(twowindow, text="Scissors", height=2, width=7, font=("arial", 25), command= lambda: play2("Scissors"))
    scissors.grid(row=1, column=2)

def play1(play1choose):
    pass
def play2(play2choose):
    pass
window = Tk()
which = Label(window, text="What do you want to play?", font=("arial", 25))
which.grid(row=0, column=1)
twoplay = Button(window, text="2 Player", font=("arial", 25), command= lambda: twowork())
twoplay.grid(row=1, column=0)
botopt = Button(window, text="Bot", font=("arial", 25), command= lambda: botwork())
botopt.grid(row=1, column=2)
window.mainloop()