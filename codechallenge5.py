print("Odd number Summation")

tot = 0

for x in range(0, 10, 1):
    n = eval(input("Enter any number---> "))
    if n % 2:
        tot += n
print("The sum of all the given odd number is",tot)