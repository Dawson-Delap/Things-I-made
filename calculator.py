equa = input("What do you want to calculate? (put spaces inbetween characters)")
numlist = equa.split(" ")
num1 = int(numlist[0])
op = numlist[1]
num2 = int(numlist[2])
if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/" or op == "%":
    print(num1 / num2)
elif op == "*" or op == "x":
    print(num1 * num2)