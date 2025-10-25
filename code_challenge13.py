statement = True
sum = 0
odd = ""
while statement is True:
    number = eval(input("Input a random number --> "))

    if number % 2 != 0:
        print("ODD NUMBER DETECTED, code continues")
        sum +=  number
        odd += str(number) + " "
        continue
    elif number == 0 :
        print("Program stop ...")
        break
    else:
        if number % 2 == 0 :
            print("EVEN NUMBER DETECTED, code continues")
        else:
            print("Invalid input")
            continue
print(f"HI, the sum of all odd number is {sum}")
print(f" odd number include the ff {odd}")