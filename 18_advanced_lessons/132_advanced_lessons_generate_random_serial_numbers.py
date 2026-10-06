# Lesson 132 - Advanced Lessons - Generate Random Serial Numbers
# Video: https://www.youtube.com/watch?v=GW78NkdM7bU

# --------------------------------------------------------
# -- Advanced_Lessons => Generate Random Serial Numbers --
# --------------------------------------------------------

import string, random

# print(string.digits) # 0123456789
# print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
# print(string.ascii_lowercase) # abcdefghijklmnopqrstuvwxyz
# print(string.ascii_uppercase) # ABCDEFGHIJKLMNOPQRSTUVWXYZ
# print(string.punctuation) # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
# print(string.hexdigits) # 0123456789abcdefABCDEF
# print(string.octdigits) # 01234567

# print(string.printable) # 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~        
# printable -> كل اشي بالإضافة الى المسافات والأسطر الجديدة

def make_serial(count):

    all_chars = string.ascii_letters + string.digits + string.punctuation

    # print(all_chars) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

    chars_count = len(all_chars)

    # print(chars_count) # 94 -> 52 حرفا + 10 أرقام + 32 رمزا

    myList = []

    while count > 0:

        myList.append(all_chars[random.randint(0,chars_count-1)])

        count -= 1

    print("".join(myList))
    
make_serial(40)

# هشغل الكود أكثر من مرة وفي كل مرة هيعطيني نص مختلف مكون من 40 حرف ورمز وعدد زي ما انا طلبت
# ملاحظة: للأمور الأمنية مثل كلمات المرور والرموز السرية استخدم المكتبة secrets بدلا من random
# لأن نتائج random يمكن توقعها، أما secrets فمصممة لتكون آمنة

# jEp7:<iP9:F/J-<B7{@k)mvGl/(u+sp=nHmS)>Mk
# tLg$PT{1j_tW.G149v,C@5Wz=y=$4G{h::{\*!'t
# <]%yB/cq4B\;S./llIB7!g#Cn|V<h@t"jlI">oa8
# $!_VYfuZrZG4HXB)(nnRg57=MMH'!E\b`>_udFy!
# ][(6V+.+892tN@\ERPS*W/{:_QAX#+6">i=VT1f-
