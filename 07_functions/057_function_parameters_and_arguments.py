# Lesson 057 - Function Parameters And Arguments
# Video: https://www.youtube.com/watch?v=CCMKMBGUxkc

# ---------------------------------------
# -- Function Parameters And Arguments --
# ---------------------------------------

a, b, c = "Mohammed", "Ahmed", "Sayed"

def say_hello(name):

    print(f"Hello {name}")

say_hello(a) # Hello Mohammed
say_hello(b) # Hello Ahmed
say_hello(c) # Hello Sayed

# def                         => Function Keyword [Define]
# say_hello()                 => Function Name
# name                        => Parameter
# print(f"Hello {name}")      => Task
# say_hello(a)                => a is The Argument

# ============================================

def addition(n1, n2):

    print(n1 + n2)

addition(20, 45) # 65
addition(-10, 30) # 20

def addition(n1, n2):

    if type(n1) != int or type(n2) != int:

        print("Only Integers Allowed")

    else:
        print(n1 + n2)

addition(20, "100") # Only Integers Allowed
addition(20, 100) # 120

# ============================================

def full_name(first, middle, last):
    print(f"Hello {first.strip().capitalize()} {middle.upper():.1s} {last.capitalize()}")

full_name("mohammed", "Alaa", "mohsen") # Hello Mohammed A Mohsen
