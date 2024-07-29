saveyear = int(input("How much do you want to save per year?"))
months = saveyear / 12
weeks = saveyear / 52

print("You want to save ", saveyear, "per year")
if saveyear >= 50000:
    print("Woah thats a lot")
else:
    print()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

print("you need to save ", months, "per month")
print("you need to save ", weeks, "per week")