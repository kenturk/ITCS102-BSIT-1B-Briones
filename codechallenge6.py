print("THE FACTORIAL PROGRAM")

n = eval(input("Enter any number ---> "))
tot = 1
for x in range(n, 0, -1):
    tot *= x
print("The factorial of",n,"is",tot)