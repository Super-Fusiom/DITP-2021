#PS
#29/10/21
#Shoping list 
shopping = [["Bread",2],["Milk",3],["Cheese",1],["Nappies", 72]]
print("*******************\n***Shopping list***\n*******************")
for shop in shopping:
    item = shop[0]
    quantity = shop[1]
    print("{}: {}".format(item, quantity))

print()
print()



#Result percentage
results = [["Maths", 75],["English", 62],["PE", 45],['DT',100]]
print('*******************\n***** Results *****\n*******************')

for result in results:
    subject = result[0]
    score = result[1]
    print("{}: {}%".format(subject, score))
print()
print()




#Result Grade
grades = [["Maths", 75],["English", 62],["PE", 45],['DT',100]]
print('*******************\n***** Results *****\n*******************')


'''Putting and in the conditions prints only one grade insted of 2
e.g if score >= 90:
        g = 'A'
    elif score >= 70:
        g = 'B' 
    
This will print out DT:AB '''

print()
for grade in grades:
    subject = grade[0]
    score = grade[1]
    if score >= 90:
        g = 'A'
    elif (score >= 70) and (score < 90):
        g = 'B'
    elif (score >= 50) and (score < 70):
        g = 'C'
    elif score < 50:
        g = 'F'
    print('{}: {}'.format(subject, g))
print()
print()



#Courses location and amount of students
courses = [['DT', 58, 'Brook'],['English', 122, 'Brook'],['Science', 95, 'Tower'],['History' ,156, 'Pipitea']]
for course in courses:
    subject = course[0]
    student = course[1]
    locale = course[2]
    print('{} is located at {} with {} students'.format(subject, locale, student))


print()
print()
#Trying code: Exercise 4 Appending 2d arrays

orders = []

while True:
    flavour = input("Enter the pizza flavor you would like, or 'quit' to complete your order: ")
    if flavour.lower()=="quit":
        break
    quantity = int(input("How many {} would you like? ".format(flavour)))
    order = [flavour, quantity]
    orders.append(order)

print('\nYour order:')
total = 0
for order in orders:
    flav = order[0]
    quan = order[1]
    total += quan