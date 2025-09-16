temp_input = input("Enter temperature: ")

if temp_input.lstrip('-').isnumeric():  # check if it's a number (negative allowed)
    temp = int(temp_input)

    if temp <= 0:
        print("The temperature is considered: Below Freezing")
    elif 1 <= temp <= 15:
        print("The temperature is considered as Extremely Cold")
    elif 16 <= temp <= 30:
        print("The temperature is considered as Cold")
    elif 31 <= temp <= 38:
        print("The temperature is considered as Lukewarm")
    elif 39 <= temp <= 42:
        print("The temperature is considered as Warm")
    elif 43 <= temp <= 50:
        print("The temperature is considered as Hot")
    elif 51 <= temp <= 60:
        print("The temperature is considered as Extremely Hot")
    elif temp >= 61:
        print("The temperature is considered as Burning")
else:
    print("Invalid temperature")