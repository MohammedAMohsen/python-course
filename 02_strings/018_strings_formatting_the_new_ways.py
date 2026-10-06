# Lesson 018 - Strings Formatting The New Ways
# Video: https://www.youtube.com/watch?v=nn4qN90A7X4

# ---------------------------------
# -- Strings Formatting New Ways --
# ---------------------------------

Name = "Mohammed"
age = 21
rank = 10

print("My Name is: {}" .format(Name)) # => My Name is: Mohammed
print("My Name is: {} And My Age is {}" .format(Name, age)) # => My Name is: Mohammed And My Age is 21
print("My Name is {} And My Age is {} And My Rank is: {}" .format(Name, age, rank)) 
print("My Name is {:s} And My Age is {:d} And My Rank is: {:f}" .format(Name, age, rank)) 

# {:s} => String
# {:d} => Number
# {:f} => Float

n = "Mohammed"
l = "Python"
y = 10

print("My Name is {} Iam {} Developer With {} Years Exp" .format(n, l, y))

# control Floating Point Number -> التحكم في عدد الأصفار

myNumber = 10
print("My Number is: {:d}" .format(myNumber))   # My Number is: 10
print("My Number is: {:f}" .format(myNumber))   # My Number is: 10.000000
print("My Number is: {:.2f}" .format(myNumber)) # My Number is: 10.00

# Truncate String -> التحكم في طول الجملة

MyLongString = "Hello Peoples of ALBasha Web School I Love You All"
print("Message is {:s}" .format(MyLongString))    # => Message is Hello Peoples of ALBasha Web School I Love You All
print("Message is {:.17s}" .format(MyLongString)) # => Message is Hello Peoples of

# Format Money -> تنسيق الأرقام الطويلة

MyMoney = 5001343334

print("My Money in Bank Is: {:d}" .format(MyMoney))  # => My Money in Bank Is: 5001343334
print("My Money in Bank Is: {:_d}" .format(MyMoney)) # => My Money in Bank Is: 5_001_343_334
print("My Money in Bank Is: {:,d}" .format(MyMoney)) # => My Money in Bank Is: 5,001,343,334
# print("My Money in Bank Is: {:,-d} or {:,&d}" .format(MyMoney)) # => Wrong

# ReArrange Items -> ترتيب العناصر

a, b, c = "One", "Two", "Three"

print("Hello {} {} {}".format(a, b, c)) # => Hello One Two Three
print("Hello {1} {2} {0}".format(a, b, c)) # => Hello Two Three One
print("Hello {2} {0} {1}".format(a, b, c)) # => Hello Three One Two

x, y, z = 10, 20, 30

print("Hello {} {} {}".format(x, y, z)) # => Hello 10 20 30
print("Hello {1:d} {2:d} {0:d}".format(x, y, z)) # => Hello 20 30 10
print("Hello {2:.1f} {0:.2f} {1:.3f}".format(x, y, z)) # => Hello 30.0 10.00 20.000


# Format in Version 3.6+ -> Formatأحدث طرق ال

MyName = "Mohammed"
MyAge = 21

print(f"My Name is: {MyName} and My Age is: {MyAge:.2f}") # => My Name is: Mohammed and My Age is: 21.00
