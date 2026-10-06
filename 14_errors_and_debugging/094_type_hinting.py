# Lesson 094 - Type Hinting
# Video: https://www.youtube.com/watch?v=J_e-r7NcwPU

# ------------------
# -- Type Hinting --
# ------------------

def say_hello(name: str) -> None: # None لأن الدالة تطبع فقط ولا ترجع أي قيمة

    print(f"Hello {name}")

say_hello("Ahmed")



def calculate(n1: int, n2: int) -> int: # int لأن الدالة ترجع عددا صحيحا

    return n1 + n2

print(calculate(34, 54)) # 88

# Hinting: فقط بستخدام انواع البيانات

# -> str
# -> int
# -> float
# -> list
# -> tuple
# ...

# هي فقط بتساعد في معرفة ما تفعلة الوظيفة او الكود اثناء الكتابة
# بايثون لا يمنعك من تمرير نوع مختلف، التلميح للقراءة والمساعدة فقط
# calculate("A", "B") # AB -> يعمل بدون خطأ رغم أن التلميح يقول int
