# Lesson 017 - Strings Formatting The Old Way
# Video: https://www.youtube.com/watch?v=m_OUIywn_XE

# ------------------------
# -- Strings Formatting --
# ------------------------

Name = "Basha"
age = 21
rank = 10

print("My Name is: "+Name)
# print("My Name is: "+Name+" and My age is: "+age) # Type Error

print("My Name is %s And My Age is %d" % (Name, age)) # => My Name is Basha And My Age is 21
print("My Name is %s And My Age is %d And My Rank is: %f" % (Name, age, rank))

# %s => String
# %d => Number
# %f => Float

n = "Mohammed"
l = "Python"
y = 10

print("My Name is %s Iam %s Developer With %d Years Exp" %(n, l, y))

# control Floating Point Number -> التحكم في عدد الأصفار

myNumber = 10
print("My Number is: %d" % myNumber)   # My Number is: 10
print("My Number is: %f" % myNumber)   # My Number is: 10.000000
print("My Number is: %.2f" % myNumber) # My Number is: 10.00

# Truncate String -> التحكم في طول الجملة

MyLongString = "Hello Peoples of ALBasha Web School I Love You All"
print("Message is %s" % MyLongString)    # => Message is Hello Peoples of ALBasha Web School I Love You All
print("Message is %.17s" % MyLongString) # => Message is Hello Peoples of
