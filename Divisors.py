# Create a program that asks the user for a number and then prints out a list of all the divisors of that number

while 1:
    try:
        y = int(input("Type any number: "))
        x = [a for a in range(1, y + 1)]
        print("The divisors of this number are:")
        v = []
        for z in x:
            if y % z == 0:
                v.append(z)
        print (v)
        break
    except ValueError:
        print()

# by github.com/Weltschmerz199
