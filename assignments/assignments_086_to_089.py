# Assignment 01

my_list = ["E", "Z", "R", 1, 2, 3]
my_tuple = ("L", "E", "O")
my_data = []
for data in zip(my_list, my_tuple):

    my_data.extend(data)

final_string = "".join(my_data).capitalize()

print(final_string) # Elzero

# -------- حل آخر ----------- #

print("".join(a + b for a,b in zip(my_list, my_tuple)).capitalize()) # Elzero

# _______________________________________________________________________________________________________
# Assignment 02

my_list1 = ["E", "L", "Z", "E", "R", "O", 1, 2]
my_tuple = ("E", "Z", "R", 1, 2, "E", "R", "O")
my_list2 = ("L", "E", "O", 1, 2, "E", "R", "O")
my_data = []

for item1, item2, item3 in zip(my_list1, my_tuple, my_list2):

    if isinstance(item1, str):
        my_data.append(item1)

final_string = "".join(my_data).capitalize()

print(final_string)

# _______________________________________________________________________________________________________
# Assignment 03

from PIL import Image

MyImage = Image.open("images/sample_squares.png")

MyNewImage1 = MyImage.crop((400, 0, 800, 400)).convert("L")

MyNewImage1.save("images/new_image_1.png")

MyNewImage2 = MyImage.crop((0, 400, 1200, 800)).convert("L").rotate(180)

MyNewImage2.save("images/new_image_2.png")

# _______________________________________________________________________________________________________
# Assignment 04

def say_hello_to(name):
    
    """
    parameter(someone) => Person Name
    Function To Say Hello To Anyone
    """

    return(f"hello {name}")

print(say_hello_to("Osama"))
print(say_hello_to.__doc__)

# _______________________________________________________________________________________________________
# Assignment 05

# == =============================== ==
# == ------- test_pylint.py -------- == ملف جديد بتسمية مناسبة وطريقة كتابة كود منسق حسب المعيار المتفق عليه
# == =============================== ==

"""
This Is My Module
To Create Function
To Print My Friends.
"""

my_friends = ["Ahmed", "Osama", "Sayed"]

def say_hello(some_peoples) -> None:

    '''This function prints hello to every friend in the list.'''

    for someone in some_peoples:

        print(f"Hello {someone}")

say_hello(my_friends)

# --------------------------------------------------------------------
# Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)
