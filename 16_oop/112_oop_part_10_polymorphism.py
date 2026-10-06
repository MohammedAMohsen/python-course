# Lesson 112 - OOP Part 10 -  Polymorphism
# Video: https://www.youtube.com/watch?v=eaGhE6EpmBI

# --------------------------------------------------------
# -- Object Oriented Programming => Polymorphism ---------
# --------------------------------------------------------
# ميثود لها نفس الإسم ولكن بعمل اشياء مختلفة (تعدد الأوجه)
# --------------------------------------------------------

n1 = 10
n2 = 20

print(n1 + n2) # 30

s1 = "Hello"
s2 = "Python"

print(s1 + " " + s2) # Hello Python

print(len([1,2,3,4,5,6,7])) # 7
print(len("Mohammed ALbasha")) # 16
print(len({"key_one": 1, "key_two": 2, "key_three": 3})) # 3

# لاحظ العلامة + والدالة len استخدمناها مع أنواع مختلفة وأعطتنا نتائج مختلفة

class A:

    def do_something(self):
        
        print("From Class A")

        raise NotImplementedError("Derived Class Must Implement This Method")
#       هذا الأمر يلزم اي شخص يقوم بعمل وراثة من هذا الكلاس انو ينشاء مثل هذة الميثود
#       Override اي انو يعمل 
#       مش الزامي هذا الأمر ممكن اترك مساحة للمستخدم


class B(A):

    def do_something(self):
        
        print("From Class B")

class C(A):

    def do_something(self):
        
        print("From Class C")


my_instance = B()

my_instance.do_something() # From Class B

# لو لم نضف الميثود في الكلاس B لنفذ ميثود الكلاس A، فيطبع ثم يظهر الخطأ
# From Class A
# NotImplementedError: Derived Class Must Implement This Method
# لذلك لازم اضيف الميثود (Override) في الكلاس الثاني عشان تعمل بدون خطأ

# ------------------------------------------------

my_instance2 = C()

my_instance2.do_something() # From Class C

# نفس الفكرة: لولا الميثود في الكلاس C لظهر الخطأ
# NotImplementedError: Derived Class Must Implement This Method

# ------------------------------------------------

# وهنا ينتهي الدرس وهنلاحظ وجود نفس الميثود في اكثر من مكان (كلاس) وتعتطي نتائج مختلفة
