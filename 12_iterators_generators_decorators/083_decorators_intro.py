# Lesson 083 - Decorators - Intro
# Video: https://www.youtube.com/watch?v=BnBJVh1DBGw

# -------------------------
# -- Decorators => Intro -- (التزيين)
# -------------------------
# [1] Sometimes Called Meta Programming
# [2] Everything in Python is Object Even Functions
# [3] Decorator Take A Function and Add Some Functionality and Return It
# [4] Decorator Wrap Other Function and Enhance Their Behaviour
# [5] Decorator is Higher Order Function (Function Accept Function As Parameter)
# ----------------------------------------------------------------------

def myDecorators(func) : # Decorators

    def nestedFunc(): # Any Name Is Just For Decoration

        print("Before") # Message From Decorators

        func() # Execute Function

        print("After") # Message From Decorators

    return nestedFunc # Return The New Function

# ----------------

def sayhello():

    print("Hello From Say Hello Function")

sayhello() # Hello From Say Hello Function

afterDecoration = myDecorators(sayhello)

afterDecoration()

# Before
# Hello From Say Hello Function
# After

# ------------------------------------------------------------------------------------------------
# هل انا مطالب اعمل هيك بالطريقة الغبية هادي .... لأ في طريقة ثانية اسمها طريقة السكر الجميل
# الي بدي انشأو functionالتي انشأته قبل اسم ال Decoratorsالطريقة ببساطة علامة ال@ مع اسم ال
# ------------------------------------------------------------------------------------------------

@myDecorators
def SayHello():

    print("Hello From Say Hello Function")

SayHello()

# Before
# Hello From Say Hello Function
# After

@myDecorators
def SayHowAreYou():

    print(f"Hello From Say How Are You Function")

SayHowAreYou()

# Before
# Hello From Say How Are You Function
# After
