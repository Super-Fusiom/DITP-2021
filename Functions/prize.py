#welcome to the prize game
#list of prizes
prizelist = ["Holiday to North Korea","Framework DIY Edtion","Banana","Bioshock Collection","0.0001 bitcoin"]

#ask for number

prizenum = int(input('Pick a number between 1 to 5 to choose your prize: '))

#what is the prize calculator
#-1 due to indexing
prize = prizelist[prizenum - 1]
print('Congratulations you have won',prize)