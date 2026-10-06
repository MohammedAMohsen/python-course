# Lesson 084 - Decorators - Function With Parameters
# Video: https://www.youtube.com/watch?v=ZVCPwfyAcBE

# --------------------------------------------
# -- Decorators => Function With Parameters --
# --------------------------------------------

def myDecorators(func):

    def nestedFunc(num1, num2): # تبعتي بنفس العدد funcبضيف البراميتر الي همررهم لل

        if num1 < 0 or num2 < 0:

            print("Beware One Of The Numbers Is Less Than Zero")

        func(num1, num2) # وأيضا بكتب البراميتر هنا كمان

    return nestedFunc

def myDecoratorsTwo(func):

    def nestedFunc(num1, num2):

        print("Coming From Decorator Two")

        func(num1, num2)

    return nestedFunc

# Functionعلى نفس ال Decorators بقدر استخدم اكثر من 

@myDecorators
@myDecoratorsTwo
def Calculate(n1, n2):

    print(n1 + n2)

Calculate(10, 20)

# Coming From Decorator Two
# 30

Calculate(-10, 20)
# Beware One Of The Numbers Is Less Than Zero
# Coming From Decorator Two
# 10


