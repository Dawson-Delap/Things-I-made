print('''_|_|_
_|_|_
 | | ''')
a1 = "_"
b1 = "_"
c1 = "_"
a2 = "_"
b2 = "_"
c2 = "_"
a3 = " "
b3 = " "
c3 = " "
win = 0
def xturn():
    xplace = input('''  You are X's!
    Where do you want to go? 
    (colums: a-c)
    (rows: 1-3)
    (ex: a1)
    ''')
    global a1
    global a2
    global a3
    global b1
    global b2
    global b3
    global c1
    global c2
    global c3
    global win
    if xplace == "a1":
        if a1 != "O":
            a1 = "X"
        else:
            print("!!!!!!!!!!!!!!!!!!!!Already taken!!!!!!!!!!!!!!!!!!!!!!!!")
            xturn()
    elif xplace == "b1":
        if b1 != "O":
            b1 = "X"
        else:
            print("!!!!!!!!!!!!!!!!!!!!Already taken!!!!!!!!!!!!!!!!!!!!!!!!")
            xturn()
    elif xplace == "c1":
        if c1 != "O":
            c1 = "X"
        else:
            print("!!!!!!!!!!!!!!!!!!!!Already taken!!!!!!!!!!!!!!!!!!!!!!!!")
            xturn()
    elif xplace == "a2":
        if a2 != "O":
            a2 = "X"
        else:
            print("!!!!!!!!!!!!!!!!!!!!Already taken!!!!!!!!!!!!!!!!!!!!!!!!")
            xturn()
    elif xplace == "b2":
        if b2 != "O":
            b2 = "X"
        else:
            print("!!!!!!!!!!!!!!!!!!!!Already taken!!!!!!!!!!!!!!!!!!!!!!!!")
            xturn()
    elif xplace == "c2":
        if c2 != "O":
            c2 = "X"
        else:
            print("!!!!!!!!!!!!!!!!!!!!Already taken!!!!!!!!!!!!!!!!!!!!!!!!")
            xturn()
    elif xplace == "a3":
        if a3 != "O":
            a3 = "X"
        else:
            print("!!!!!!!!!!!!!!!!!!!!Already taken!!!!!!!!!!!!!!!!!!!!!!!!")
            xturn()
    elif xplace == "b3":
        if b3 != "O":
            b3 = "X"
        else:
            print("!!!!!!!!!!!!!!!!!!!!Already taken!!!!!!!!!!!!!!!!!!!!!!!!")
            xturn()
    elif xplace == "c3":
        if c3 != "O":
            c3 = "X"
        else:
            print("!!!!!!!!!!!!!!!!!!!!Already taken!!!!!!!!!!!!!!!!!!!!!!!!")
            xturn()
    else:
        print("Invalid place")
        oturn()

    if a1 == "X" and a2 == "X" and a3 == "X":
        win = win + 1
        print("X's WIN!")
    if b1 == "X" and b2 == "X" and b3 == "X":
        win = win + 1
        print("X's WIN!")
    if c1 == "X" and c2 == "X" and c3 == "X":
        win = win + 1
        print("X's WIN!")
    if a1 == "X" and b1 == "X" and c1 == "X":
        win = win + 1
        print("X's WIN!")
    if a2 == "X" and b2 == "X" and c2 == "X":
        win = win + 1
        print("X's WIN!")
    if a3 == "X" and b3 == "X" and c3 == "X":
        win = win + 1
        print("X's WIN!")
    if a1 == "X" and b2 == "X" and c3 == "X":
        win = win + 1
        print("X's WIN!")
    if a3 == "X" and b2 == "X" and c1 == "X":
        win = win + 1
        print("X's WIN!")


    board = f'''{a1}|{b1}|{c1}
{a2}|{b2}|{c2}
{a3}|{b3}|{c3} '''
    print(board)

def oturn():
    oplace = input('''  You are O's!
    Where do you want to go? 
    (colums: a-c)
    (rows: 1-3)
    (ex: a1)
    ''')
    global a1
    global a2
    global a3
    global b1
    global b2
    global b3
    global c1
    global c2
    global c3
    if oplace == "a1":
        if a1 != "X":
            a1 = "O"
        else:
            print("!!!!!!!!!!!!!!!!!!!!Already taken!!!!!!!!!!!!!!!!!!!!!!!!")
            oturn()
    elif oplace == "b1":
        if b1 != "X":
            b1 = "O"
        else:
            print("!!!!!!!!!!!!!!!!!!!!Already taken!!!!!!!!!!!!!!!!!!!!!!!!")
            oturn()
    elif oplace == "c1":
        if c1 != "X":
            c1 = "O"
        else:
            print("!!!!!!!!!!!!!!!!!!!!Already taken!!!!!!!!!!!!!!!!!!!!!!!!")
            oturn()
    elif oplace == "a2":
        if a2 != "X":
            a2 = "O"
        else:
            print("!!!!!!!!!!!!!!!!!!!!Already taken!!!!!!!!!!!!!!!!!!!!!!!!")
            oturn()
    elif oplace == "b2":
        if b2 != "X":
            b2 = "O"
        else:
            print("!!!!!!!!!!!!!!!!!!!!Already taken!!!!!!!!!!!!!!!!!!!!!!!!")
            oturn()
    elif oplace == "c2":
        if c2 != "X":
            c2 = "O"
        else:
            print("!!!!!!!!!!!!!!!!!!!!Already taken!!!!!!!!!!!!!!!!!!!!!!!!")
            oturn()
    elif oplace == "a3":
        if a3 != "X":
            a3 = "O"
        else:
            print("!!!!!!!!!!!!!!!!!!!!Already taken!!!!!!!!!!!!!!!!!!!!!!!!")
            oturn()
    elif oplace == "b3":
        if b3 != "X":
            b3 = "O"
        else:
            print("!!!!!!!!!!!!!!!!!!!!Already taken!!!!!!!!!!!!!!!!!!!!!!!!")
            oturn()
    elif oplace == "c3":
        if c3 != "X":
            c3 = "O"
        else:
            print("!!!!!!!!!!!!!!!!!!!!Already taken!!!!!!!!!!!!!!!!!!!!!!!!")
            oturn()
    else:
        print("invalid place")
        oturn()
    
    if a1 == "O" and a2 == "O" and a3 == "O":
        win = win + 1
        print("O's WIN!")
    if b1 == "O" and b2 == "O" and b3 == "O":
        win = win + 1
        print("O's WIN!")
    if c1 == "O" and c2 == "O" and c3 == "O":
        win = win + 1
        print("O's WIN!")
    if a1 == "O" and b1 == "O" and c1 == "O":
        win = win + 1
        print("O's WIN!")
    if a2 == "O" and b2 == "O" and c2 == "O":
        win = win + 1
        print("O's WIN!")
    if a3 == "O" and b3 == "O" and c3 == "O":
        win = win + 1
        print("O's WIN!")
    if a1 == "O" and b2 == "O" and c3 == "O":
        win = win + 1
        print("O's WIN!")
    if a3 == "O" and b2 == "O" and c1 == "O":
        win = win + 1
        print("O's WIN!")
        


    board = f'''{a1}|{b1}|{c1}
{a2}|{b2}|{c2}
{a3}|{b3}|{c3} '''
    print(board)
while win == 0:
    xturn()
    oturn()

    
