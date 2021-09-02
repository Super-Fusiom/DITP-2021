target = 2000000
pay = float(input("How much do you earn per week: "))
bills = float(input("How much is all of your bills per week: "))
savings = pay - bills
while savings < target:
    week =+ 1
    savings = pay - bills
print("You can retire at ", week,"from now!")
