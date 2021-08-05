
bank_charge = 10
bank_balance = 100
bonus = 5
while True:
    print("You have ", bank_balance , "in your bank account")
    if bank_balance <= bank_charge:
        print("Noice you get a bonus")
        bank_balance += bonus
    else:
        print('Bank charges may apply...')
        bank_balance -= bank_balance
    choice = input("Do you want to withdraw or not")
    if choice == "y":
        print("How much do you want to withdraw?\n")
        w_amount = float(input())
        bank_balance -= w_amount
        print("Noice you have ", bank_balance , "in the bank")