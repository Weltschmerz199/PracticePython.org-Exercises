#Take two lists and write a program that returns a list that contains
# only the elements that are common between the lists (without duplicates).
# Make sure your program works on two lists of different sizes.

import random
x = [random.randint(1, 99) for i in range(1, 20)]
y = [random.randint(1, 99) for i in range(1, 15)]
z = []
print ("1th random list of numbers: " + str(x))
print ("2th random list of numbers: " + str(y))
for i in x:
    for c in y:
        if c == i:
            z.append(i)
print ("Elements common to both lists: " + str(sorted(set(z))))

# by github.com/Weltschmerz199