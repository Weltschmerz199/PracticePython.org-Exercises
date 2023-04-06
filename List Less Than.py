#1: Take a list and write a program that prints out all the elements of the list that are less than 5.
#2: Instead of printing the elements one by one, make a new list that has all the elements less than 5
#from this list in it and print out this new list.
#3: Ask the user for a number and return a list that contains only elements from the original list a that
#are smaller than that number given by the user

import random
x = [random.randint(1, 99) for i in range(1, 20)]
print ("random collection: " + str(sorted(x)))
while 1:
    try:
        y = int(input("Type number: "))
        v = []
        q = []
        for z in x:
            if z < 5:
                q.append(z)
            if z < y:
                v.append(z)
        print("Elements of the set smaller than the typed number: " +str(sorted(v)))
        print("Elements of the set smaller than 5: " + str(sorted(q)))
        break
    except ValueError:
        print()

# by github.com/Weltschmerz199
