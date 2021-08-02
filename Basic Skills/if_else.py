#Creator:Paul Singh
#Date:2/8/21

#Babysitting Club

#Required age is 14 to be in the club
minage = 14
#Greeting 
print("Welcome to the Babysitting Club!!!")
print("We are looking for new babysitters!")
print("You must be at least",minage," to be a babysitter\n")
#Colleting user's name and age
name = input("What is your name: ")
age = int(input("How old are you? "))
#Check if user is under 14, if so then decline.
#If they are over 14 then approve
if age < minage:
	print("Sorry",name,', ', age, "is too young to be a babysitter.")
else:
	print(name,',',age,"is a great age to be a babysitter.")
