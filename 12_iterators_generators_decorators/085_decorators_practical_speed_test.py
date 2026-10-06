# Lesson 085 - Decorators - Practical Speed Test
# Video: https://www.youtube.com/watch?v=WQk_j8KMExY

# ----------------------------------------
# -- Decorators => Practical Speed Test --
# ----------------------------------------

def myDecorators(func):

    def nestedFunc(*number): # هان بقدر امرر اكثر من براميتر او 0 براميتر

        for num in number:

            if num < 0:

                print("Beware One Of The Numbers Is Less Than Zero")

        func(*number)

    return nestedFunc

@myDecorators
def Calculate(n1, n2, n3, n4):
    print(n1 + n2 + n3 + n4)

Calculate(10, 20, 42, 21) # 93

Calculate(10, 20, 42, -21) # 51
# Beware One Of The Numbers Is Less Than Zero
# 51

# ------------------------------------------------------------

# Example Of The Day :) ... أثناء عملها functionحساب كم استغرقت وقت ال

from time import time

def speedTest(fun):

    def wrapper():

        start = time() # تبدأ funالوقت قبل ما ال

        fun()

        end = time() # انتهت funالوقت بعد ما ال
        
        print(f"Function Running Time Is: {(end - start):.2f}") # الوقت المستغرق

    return wrapper

@speedTest
def bigLoop():
    for n in range(0, 30000):
        print(n)

bigLoop()

# 1
# 2
# 3
# .
# .
# .
# .
# 29997
# 29998
# 29999
# Function Running Time Is: 2.30 -> الوقت يختلف حسب سرعة جهازك
