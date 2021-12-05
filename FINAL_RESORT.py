
def camp_name():
    print("*****************************\n*** Sunshine Holiday camp ***\n*****************************")





camp_name()
#Getting user info
name = input("What is your name: ")
age = int(input("What is your age: "))
#Check if user is eligible for entry and if the user is under 10
if (age >= 7) and (age <= 12):
    if age < 10:
        veg_orders = []
        vegtables = ['Spinach', 'Carrots', 'Broccoli', 'Garlic','Brussel Sprouts']
        while True:
            if veg_orders == False:
                break
            print('Here are the lists of vegtables: ')
            for x in range(len(vegtables)):
                print (vegtables[x])
            while True:
                veg = input('Pick a vegtable:')
                if (veg != vegtables[0]) or (veg != vegtables[1]) or (veg != vegtables[2]) or (veg != vegtables[3]) or (veg != vegtables[4]):
                    print('Type a vegtable from the list')
                else:
                    break
            while True:
                try:
                    quantity = int(input('How many would you like? ')
                    break
                except ValueError:
                    print('Number please!')
            veg_order = [veg, quantity]
            veg_orders.append(veg_order)
        print()
    else:
        print('Your name is {} and you are {} years old.'.format(name, age))
else:
    print('You are not eligable to join')
camp_name()




