import random
def bot():
    ran = ["rock", "paper", "scissors"]
    opt = random.choice(ran)
    play = input('''rock paper or scissors:
(All lower case)
''')
    print("Bot chose: ", opt)
    win = 0
    if play == "rock" and opt == "scissors":
        win = 1
        print("You win!")
    if play == "paper" and opt == "rock":
        win = 1
        print("You win!")
    if play == "scissors" and opt == "paper":
        win = 1
        print("You win!")
    if opt == "rock" and play == "scissors":
        win = 1
        print("Bot wins ;(")
    if opt == "paper" and play == "rock":
        win = 1
        print("Bot wins ;(")
    if opt == "scissors" and play == "paper":
        win = 1
        print("Bot wins ;(")

        if play == opt:
            print("Tied!")

def play2():
    play = input('''Player 1:
rock paper or scissors:
(All lower case)
''')
    for i in range(0,50):
        print("|")
    plays = input('''Player 2:
rock paper or scissors:
(All lower case)
''')
    win = 0
    if play == "rock" and plays == "scissors":
        win = 1
        print("Player 1 wins!")
    if play == "paper" and plays == "rock":
        win = 1
        print("Player 1 wins!")
    if play == "scissors" and plays == "paper":
        win = 1
        print("Player 1 wins!")
    if plays == "rock" and play == "scissors":
        win = 1
        print("Player 2 wins!")
    if plays == "paper" and play == "rock":
        win = 1
        print("Player 2 wins!")
    if plays == "scissors" and play == "paper":
        win = 1
        print("Player 2 wins!")

        if play == plays:
            print("Tied!")

which = input('''What do you want to play:
(2 player or bot:)

''')

if which == "bot":
    bot()
if which == "2 player":
    play2()
