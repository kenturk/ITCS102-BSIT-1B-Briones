words = input("Enter the Word that you like: ")
numbers = len(words)
n = 0
num1 = []
print(f"The Word That You Choose have {numbers} letters\n")
for i in range (1,numbers+1):
    num = int(input(f"Enter the {i} number: "))
    n += num
    num1.append(num)
 
print(f"The Numbers That you enter are \n",num1)
print(f"The Total Numbers are: {n}\n")
ave = n / numbers
print(f"The average wavelenght are: {ave}")