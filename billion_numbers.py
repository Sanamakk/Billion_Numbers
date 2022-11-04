from random import randint
#Generate random numbers

#2 billion of numbers
count = 2 * 1000 * 1000 * 1000
for _ in range (count):
    #Randon number between 0 and 10
    value = randint(0,10)
    value2 = str(value)
    #if value is 5, print a new line
    if value !=5:
        print(value2, end =' ')
    else:
        print(value2)
    
