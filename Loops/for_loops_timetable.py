#Mutiplication Generator
#1/9/21
#Super_Fusiom

#Get number from user for number to generate times table

num = int(input("Enter your number: "))
times = int(input("How many times?: "))

for answer in range (1,times+1):
    print(num,"*",answer,"=", num*answer)