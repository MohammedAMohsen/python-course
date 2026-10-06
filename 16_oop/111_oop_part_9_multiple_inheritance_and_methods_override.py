# Lesson 111 - OOP Part 9 - Multiple Inheritance And Method Overriding
# Video: https://www.youtube.com/watch?v=OwfiogOFIF4

# ---------------------------------------------------------
# -- Object Oriented Programming => Multiple Inheritance --
# ---------------------------------------------------------

class BaseOne:

    def __init__(self):

        print("Base One")
    
    def func_one(self):

        print("One")

class BaseTwo:
        
    def __init__(self):

        print("Base Two")

    def func_two(self):

        print("Two")

class Derived(BaseOne, BaseTwo):

    pass



my_var = Derived() # Base One -> (class Derived(BaseOne, BaseTwo)) طبع من الكلاس الأول بسبب الترتيب في الوراثة

# class.mro -> بيظهر ترتيب الوراثة في الكلاس

print(Derived.mro()) # [<class '__main__.Derived'>, <class '__main__.BaseOne'>, <class '__main__.BaseTwo'>, <class 'object'>]

# -----------------------------------------

# العنوان 0x... يختلف في كل تشغيل
print(my_var.func_one) # <bound method BaseOne.func_one of <__main__.Derived object at 0x7742c9b02e40>>
print(my_var.func_two) # <bound method BaseTwo.func_two of <__main__.Derived object at 0x7742c9b02e40>>

my_var.func_one() # One
my_var.func_two() # Two

# -----------------------------------------


class Base:

    pass

class DerivedOne(Base):

    pass
                              # (DerivedTwo) -> Inheritance ->  (DerivedOne) -> Inheritance -> (Base)
class DerivedTwo(DerivedOne): # (DerivedTwo) -> Inheritance -> (Base)

    pass
