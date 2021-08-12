#Input age and weight (includes limits)
age = int(input("How old are you? "))
weight = float(input("What is your weight? "))
age_limit_low = 16
weight_limit_low = 50
age_limit_high = 70
#check if user meets the requirements for donating blood
if age >= age_limit_low and weight >= weight_limit_low and age <= age_limit_high:
    print('Noice you can donate blood')
else:
    print("Oh noes, you can't donate blood")
