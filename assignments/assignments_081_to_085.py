# Assignment 01

def reverse_string(my_string):

#   for my in my_string[::-1]: ممكن بهذه الطريقة
    for my in reversed(my_string):

        yield my

TheName = reverse_string("Mohammed")

print(next(TheName))
print(next(TheName))
print(next(TheName))
print(next(TheName))
for c in TheName:
    print(c)

# _______________________________________________________________________________________________________
# Assignment 02

import termcolor

def myDecorator(myfun):
    def NestedFunc():
        print(termcolor.colored("Sugar Added From Decorators","yellow",attrs=["bold"]))
        myfun()
        print(termcolor.colored("---------------------------","yellow",attrs=["bold"]))
    return NestedFunc

@myDecorator
def make_tea():
    print("Tea Created")

@myDecorator
def make_coffee():
    print("Coffee Created")

make_tea()
make_coffee()