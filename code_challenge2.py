money = eval(input("Enter the amount to deposit-->: "))

thousand = money // 1000    # Using floor division to count how many "thousands"
R_amount1 = money % 1000  # Remaining amount after thousands    

#basta magiging variable yung mga "name =" and then kasunod ng "=" yung math and then so on and so forth

five_hundred = R_amount1 // 500 #Remaining amount after thousands and then floor division by 500
R_amount2 = R_amount1 % 500 #Remaining amount after five hundreds

two_hundred = R_amount2 // 200
R_amount3 = R_amount2 % 200

one_hundred = R_amount3 // 100
r_amount4 = R_amount3 % 100

fifty = r_amount4 // 50
r_amount5 = r_amount4 % 50

twenty = r_amount5 // 20
r_amount6 = r_amount5 % 20

ten = r_amount6 // 10
r_amount7 = r_amount6 % 10

five = r_amount7 // 5
r_amount8 = r_amount7 % 5

one = r_amount8 // 1
r_amount9 = r_amount8 % 1


print("Here is a breakdown of the deposited amount:\n")
print( thousand, "-1000") #the variable is thousand and output is -1000
print( five_hundred, "-500")
print( two_hundred, "-200")
print( one_hundred, "-100")
print( fifty, "-50")
print( twenty, "-20")
print( ten, "-10")
print( five, "-5")
print( one, "-1")