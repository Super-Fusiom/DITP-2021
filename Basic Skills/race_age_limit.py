"""If age is less or equal to 10 years, 
race length is 100m
else the race length is 200m"""
age = int(input("How old are you? "))
if age <= 10:
    print('The race length is 100m')
    race_length = 100
else:
    print('The race lenght is 200m')
    race_length = 200
print("All competitors must run the race distance")