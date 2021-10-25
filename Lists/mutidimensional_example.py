



#Example 1
students = [["Sally", 15], ["Regina", 16], ["Anne", 15], ["Lila", 14], ["Maleah", 16]]

for student in students:
    print(student)

print()
#Example 2
students = [["Sally", 15], ["Regina", 16], ["Anne", 15], ["Lila", 14], ["Maleah", 16]]

for student in students:
    print(student[0])
    print(student[1])

print()
#Example 3
students = [["Sally", 15], ["Regina", 16], ["Anne", 15], ["Lila", 14], ["Maleah", 16]]

for student in students:
    name = student[0]
    age = student[1]
    print('{} is {}'.format(name, age))