# Assignment 01

import random

print(f"Random Number Between 10 And 50 => {random.randint(10,50)}")

print(f"Random Even Number Between 2 And 10 => {random.randrange(2,11,2)}")

print(f"Random Odd Number Between 1 And 9 => {random.randrange(1,10,2)}")

print(dir(random))

# _______________________________________________________________________________________________________
# Assignment 02

import my_mod

my_mod.say_hello("Mohammed")
my_mod.say_welcome("Mohammed")

# _______________________________________________________________________________________________________
# Assignment 03

from my_mod import say_welcome

say_welcome("Mohammed")

# _______________________________________________________________________________________________________
# Assignment 04

from my_mod import say_welcome as new_welcome

new_welcome("Mohammed")
