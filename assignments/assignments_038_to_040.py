# Assignment 01

name = input("Please Write Your Name: ").strip().capitalize()
print(f"Hello {name}, Happy To See You Here.")
# _______________________________________________________________________________________________________
# Assignment 02

age = int(input("Please Write Your Age: "))
if age > 16:
    print(f"Hello Your Age Is {age}, All Articles Is Suitable For You")
else:
    print("Hello Your Age Is Under 16, Some Articles Is Not Suitable For You")
# _______________________________________________________________________________________________________
# Assignment 03

first_name = input("Please Enter Your First Name: ").strip().capitalize()
second_name = input("Please Enter Your Last Name: ").strip().capitalize()
print(f"Hello {first_name} {second_name:.1s}")
# _______________________________________________________________________________________________________
# Assignment 04

email = input("Please Enter Your Email: ").strip().lower()

print(f"Your Name Is {email[:email.index('@')].capitalize()}")
print(f"Email Service Provider Is {email[email.index('@')+1:email.index('.')]}")
print(f"Top Level Domain Is {email[email.index('.')+1:]}")
