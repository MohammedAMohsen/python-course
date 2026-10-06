# Lesson 046 - Practical Membership Control
# Video: https://www.youtube.com/watch?v=r9MaqQ0Iis0

# ----------------------------------
# -- Practical Membership Control --
# ----------------------------------

# List Contains Admins
admins = ["Ahmed", "Mohammed", "Sameh", "Manal", "Rahma", "Mahmoud", "Enas"]

# Login 

name = input('Please Type Your Name ').strip().capitalize()

# If Name Is In Admins

if name in admins :

    print(f"Hello {name} Welcome Back")

    option = input('Delete Or Update Your Name? ').strip().capitalize()

    # Update Option
    if option == "Update" or option == "U":

        theNewName = input('Your New Name Please ').strip().capitalize()

        admins[admins.index(name)] = theNewName

        print("Name Updated.")

        print(admins)

    # Delete Option
    elif option == "Delete" or option == "D":

        admins.remove(name)
        
        print("Name Deleted")

        print(admins)
    
    else : print("Wrong Option Chosen")

else :

    status = input('Not Admin, Add You Y, N? ').strip().capitalize()

    if status == "Yes" or status == "Y":

        print("You Have Been Added")

        admins.append(name)

        print(admins)
    
    else:

        print("You Are Not Added.")
