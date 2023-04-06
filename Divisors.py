# Create a program that asks the user for a number and then prints out a list of all the divisors of that number

while 1:
    try:
        y = int(input("Type any number: "))
        x = [a for a in range(1, y + 1)]
        print("The divisors of this number are:")
        for z in x:
            if y % z == 0:
                print (z)
        break
    except ValueError:
        print()

# by www.github.com/Weltschmerz199
