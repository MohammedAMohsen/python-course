# Lesson 059 - Function Default Parameters
# Video: https://www.youtube.com/watch?v=BNXasw_j4sY

# ---------------------------------
# -- Function Default Parameters --
# ---------------------------------

# لازم يكون آخر واحد, إذا ما كان آخر واحد لازم كل الي بعدو تعطيلو قيمة إفتراضية parameterلو بدك تعمل قيمة إفتراضية ل

def say_Hello(name="UnKnown", age="UnKnown", country="UnKnown"):
# في حال ما كتب البلد أو العمر أو الإسم UnKnown القيمة الإفتارضية للبلد و للإسم والعمر  

    print(f"Hello {name} Your Age is {age} And Your Country is {country}")

say_Hello("Mohammed", 21, "Gaza") # Hello Mohammed Your Age is 21 And Your Country is Gaza
say_Hello("Sayed", 19, "Egypt") # Hello Sayed Your Age is 19 And Your Country is Egypt
say_Hello("Maha", 30, "KSA") # Hello Maha Your Age is 30 And Your Country is KSA
say_Hello("Soso", 35) # Hello Soso Your Age is 35 And Your Country is UnKnown
say_Hello("Ramy") # Hello Ramy Your Age is UnKnown And Your Country is UnKnown
say_Hello() # Hello UnKnown Your Age is UnKnown And Your Country is UnKnown
