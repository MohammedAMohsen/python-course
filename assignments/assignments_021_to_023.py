# Assignment 01

friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

print(friends[0])
print(friends.pop(0))
print(friends[-1])
print(friends.pop(-1))

# Osama
# Osama
# Mahmoud
# Mahmoud
# _______________________________________________________________________________________________________
# Assignment 02

friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

print(friends[::2])
print(friends[1::2])

# ['Osama', 'Sayed', 'Mahmoud']
# ['Ahmed', 'Ali']
# _______________________________________________________________________________________________________
# Assignment 03

friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

print(friends[1:-1])
print(friends[-2: ])

# ['Ahmed', 'Sayed', 'Ali']
# ['Ali', 'Mahmoud']
# _______________________________________________________________________________________________________
# Assignment 04

friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

friends[-2: ] = ["Elzero", "Elzero"]

print(friends) 
# ['Osama', 'Ahmed', 'Sayed', 'Elzero', 'Elzero']
# _______________________________________________________________________________________________________
# Assignment 05

friends = ["Osama", "Ahmed", "Sayed"]

friends.insert(0, "Mohammed")
friends.append("Abd")

print(friends)
# ['Mohammed', 'Osama', 'Ahmed', 'Sayed', 'Abd']
# _______________________________________________________________________________________________________
# Assignment 06

friends = ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]

friends[0:2] = []
print(friends)
friends.remove(friends[-1])
print(friends)

# ['Ahmed', 'Sayed', 'Salem']
# ['Ahmed', 'Sayed']
# _______________________________________________________________________________________________________
# Assignment 07

friends = ["Ahmed", "Sayed"]
employees = ["Samah", "Eman"]
school = ["Ramy", "Shady"]

friends.extend(employees)
friends.extend(school)

print(friends) 
# ['Ahmed', 'Sayed', 'Samah', 'Eman', 'Ramy', 'Shady']
# _______________________________________________________________________________________________________
# Assignment 08

friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]

friends.sort()
print(friends)
friends.sort(reverse=True)
print(friends)

# ['Ahmed', 'Eman', 'Ramy', 'Samah', 'Sayed', 'Shady']
# ['Shady', 'Sayed', 'Samah', 'Ramy', 'Eman', 'Ahmed']
# _______________________________________________________________________________________________________
# Assignment 09

friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]

print(len(friends)) # 6
# _______________________________________________________________________________________________________
# Assignment 10

technologies = ["Html", "CSS", "JS", "Python", ["Django", "Flask", "Web"]]

print(technologies[-1][0])
print(technologies[-1][-1])

# Django
# Web