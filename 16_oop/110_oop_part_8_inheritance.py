# Lesson 110 - OOP Part 8 - Inheritance
# Video: https://www.youtube.com/watch?v=f3Dg6gxkL-0

# ------------------------------------------------
# -- Object Oriented Programming => Inheritance --
# ------------------------------------------------

class Food: # Base Class

    def __init__(self, name, price):
        
        self.name = name
        self.price = price

        print(f"{self.name} Is Created From Base Class")

    def eat(self):

        print("Eat Method From Base Class")


class Apple(Food): # Derived Class

    def __init__(self, name, price, amount):

      # Food.__init__(self, name, price) # Create Instance From Base Class (الطريقة الأولى)

        super().__init__(name, price) # Create Instance From Base Class (الطريقة الثانية)

        self.amount = amount # -> This Attribute Is Not Inherited, It Belongs To Apple Only

        print(f"{self.name} Is Created From Derived Class And Price Is {self.price} And Amount Is {self.amount}")

    def get_from_tree(self):

        print("Get From Tree From Derived Class")



# food_one = Food("Pizza")

# food_two = Apple("Pizza", 30)
# food_two.eat() Error

# اصبحت اقدر اوصل للميثود الي في الكلاس الرئيسي Inheritance بعد ما عملت 

                                   # Pizza Is Created From Base Class   
food_two = Apple("Pizza", 30, 500) # Pizza Is Created From Derived Class And Price Is 30 And Amount Is 500
food_two.eat()                     # Eat Method From Base Class

# ----------------------------------------------

food_one = Food("Pizza", 40) # Pizza Is Created From Base Class

# food_one.get_from_tree() -> لاحظ ما بقدر يصل للميثود الي في الكلاس الفرعي او الي بياخذ من الكلاس الرئيسي

# الوراثة في اتجاه واحد: الكلاس الفرعي يرى ميثوداته وميثودات الكلاس الرئيسي
# أما الكلاس الرئيسي فلا يرى ميثودات الكلاس الفرعي

food_two.get_from_tree() # Get From Tree From Derived Class


