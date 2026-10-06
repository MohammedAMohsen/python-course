# Assignment 01

num = int(input('Enter Number: '))
count = 0

if num == 0: print("Number 0 Is Not Larger Than 0")

while num > 1:

    num -= 1

    if num != 6:

        print(num)    

        count += 1

print(f"{count} Numbers Printed Successfully.")
# _______________________________________________________________________________________________________
# Assignment 02

friends = ["Mohamed", "Shady", "ahmed", "maha", "Sherif"]
x = 0
i = 0

while len(friends) > x:
    
    if friends[x].istitle():

        print(friends[x])
    
    else:

        i += 1

    x += 1

print(f"Friends Printed And Ignored Names Count Is {i}")
# _______________________________________________________________________________________________________
# Assignment 03

skills = ["HTML", "CSS", "JavaScript", "PHP", "Python"]

while skills:

    print(skills.pop(0))
# _______________________________________________________________________________________________________
# Assignment 04

my_friends = []
MaxInput = 4

while MaxInput > 0:

    name = input('Please Enter Your Friend Name: ').strip()

    if(name.isupper()):
        print("Invalid Name")
        MaxInput += 1

    else:
        if name.istitle():
            my_friends.append(name)
            print(f"Friend {name.title()} Added")
            print(f'Names Left in List Is {MaxInput-1}')

        else:
            my_friends.append(name.title())
            print(f"Friend {name.title()} Added => 1st Letter Become Capital")
            print(f'Names Left in List Is {MaxInput-1}')

    MaxInput -= 1
    
print(my_friends)