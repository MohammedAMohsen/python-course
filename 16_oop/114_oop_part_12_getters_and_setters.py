# Lesson 114 - OOP Part 12 Getters And Setters
# Video: https://www.youtube.com/watch?v=vsOcbPE_Ih4

# ------------------------------------------------------
# -- Object Oriented Programming => Getters & Setters --
# ------------------------------------------------------

class Member:

    def __init__(self, name):
        
        self.__name = name

    def say_hello(self):

        return f"Hello {self.__name}"
    
    def get_name(self): # Getters

        return self.__name  
    
    def set_name(self, new_name): # Setters

        self.__name = new_name


# -----------------------------------

# one = Member("Mohammed")

# one._Member__name = "Osama"

# print(one._Member__name) # Osama

# :هناك طريقة افضل منها , Attributes Private الطريقة السابقة الإحتيالية لتعديل او طباعة 

# -----------------------------------

one = Member("Mohammed")

print(one.get_name()) # Mohammed

one.set_name("Mohsen")
      
print(one.get_name()) # Mohsen

# Setters و Gettersوالإستخدام الصحيح لل Attributes Privateهي الطريقة السليمة لتعديل على ال
