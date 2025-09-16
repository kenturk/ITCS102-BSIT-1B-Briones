#getting the summation of all numbers

summation = 0
for x in range(1, 11, 1):
    print("your number" ,x ,"is")
    n = eval(input("Enter any number --> "))
    summation += n
print("The sum of all the numbers is", summation)