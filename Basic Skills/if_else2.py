#Ask the person their name and age
name = input("What is your name? ")
while True:
    try:
        age = int(input("How old are you? "))
        break
    except ValueError:
        print("Number yes?")
#Using if statements to show the person what things they can do at their age
if age >= 6:
    print("At age 6 you have to go to school")
if age >= 14:
    print("At age 14 you can be left home alone")
if age >= 16:
    print("At age 16 you can your drivers licence")
if age >= 18:
    print("At age 18 you no longer get free dental")