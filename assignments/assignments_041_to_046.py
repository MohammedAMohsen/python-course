# Assignment 01

num1 = int(input('Name One: ').strip())
num2 = int(input('Name Two: ').strip())

operation = input("+ Or - Or * Or / Or % ").strip()

if   operation == "+" : print(f"The result of the operation is {num1 + num2}")
elif operation == "-" : print(f"The result of the operation is {num1 - num2}")
elif operation == "*" : print(f"The result of the operation is {num1 * num2}")
elif operation == "/" : print(f"The result of the operation is {num1 / num2}")
elif operation == "%" : print(f"The result of the operation is {num1 % num2}")
else : print("Error Input")
# _______________________________________________________________________________________________________
# Assignment 02

age = 17
print("App Is Suitable For You" if age > 16 else "App Is Not Suitable For You")
# _______________________________________________________________________________________________________
# Assignment 03

age = int(input('Please Enter Your Age ').strip())
months = age * 12
week = months * 4
days = age * 365
hours = days * 24
minutes = hours * 60
seconds = minutes * 60

if 10 < age < 100 :
    print('You Lived For:')
    print(f"{months} Months.")
    print(f"{week:,} Week.")
    print(f"{days:,} Days.")
    print(f"{hours:,} Hours.")
    print(f"{minutes:,} Minutes.")
    print(f"{seconds:,} Seconds.")
else :
    print("Age is out of range")
# _______________________________________________________________________________________________________
# Assignment 04

countries = ["Egypt", "Palestine", "Syria", "Yemen", "KSA", "USA", "Bahrain", "England"]
price = 100
discount = 30

country = input("Input Your Country ").strip().capitalize()

if country in countries:
    print(f"Your Country Eligible For Discount And The Price After Discount Is {price - discount}")
else :
    print(f"Your Country Not Eligible For Discount And The Price Is {price}")