#Program ask for username, favorite color and two favorite numbers
#Program is going to output a greeting and will do some maths

#This indicates the use of variables

#Created by Super_Fusiom (Will be using Github name)
#Created on 28/7/21

#Ask user for name
print('Enter your name')
name = input()

#Ask user for favourite color
print("what's your favorite color?")
fcolor = input()
#Ask user for favorurite numbers
print("What is your first favorite number?")
while True:
    try:
        num1 = int(input())
        break
    except ValueError:
        print("NUMBER PLEASE")
print("What is your second favorite number?")
while True:
    try:
        num2 = int(input())
        break
    except ValueError:
        print("NUMBER PLEASE")
#Do the Maths
fnum = num1 + num2
#Output Greeting and print results
print("Hi", name)
print('Your favorite color is' , fcolor)
print("Your super number is", fnum,"\nFrom the numbers" , num1 , '&' , num2)