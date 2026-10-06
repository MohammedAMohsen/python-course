# Lesson 091 - Exceptions Handling Try, Except, Else, Finally
# Video: https://www.youtube.com/watch?v=LBf_8txij3I

# -----------------------------------
# --      Exceptions Handling      --
# -- Try | Except | Else | Finally --
# -----------------------------------
# Try     => Test The Code For Errors [اجباري]
# Except  => Handle The Errors [اجباري]
# ----------------------------
# Else    => If No Errors [اختياري]
# Finally => Run The Code [اختياري]
# ------------------------


try:  # Try The Code And Test Errors

    number = int(input("write your Age: "))
    print(f"Your Age is {number}")

except:  # Handle The Errors If

    print("Bad, This is not Integer")

else:  # IF Theres No Errors

    print("Good, This Is Integer ")

finally: # ايش ما بسير عندي في البرنامج سواء خطأ او صح بنفذ هذا الأمر والكود الي داخلو

    print("Print From Finally Whatever Happens")

# حاول تنفيذ الكود اذا ما في مشاكل ودخل المستخدم رقم كمل بدون مشاكل
# الخطا وبنفذ امر معين واكمل البرنامج except في حال ادخل المستخدم حرف هان بلتقط ال 
# try لانها خاصة بال else لكن لاحظ ما بدخل على ال
# نفسها Try ايضا ولكن بالحقيقة لا تفيد كثيرا ممكن اضيف الأوامر داخل ال else وفي حال ما كان هناك اخطأ نفذ ال 

# -----------------------------------------------

# بقدر احدد نوع الخطأ الي بظهر عندي
# Exceptions بدل با يكون جميع الأخطاء بطلع نفس 


try:

    print(10 / 0)
    # print(x)

except:

    print("Cant Divide")

# output:

# Cant Divide ->  print(10 / 0)
# Cant Divide ->  print(x)

# -------------

try:

    print(10/0)
    # print(x)

except ZeroDivisionError:

    print("Cant Divide")

# output:

# Cant Divide ->  print(10 / 0)
# وهطلع من البرنامج كخطأ عام ويقف البرنامج except الي مش معرفة عندي مش هيمسكها ال x بالنسبة لمحاولة طباعة ال
# خاص فقط بالقسمة على صفر except ليش , لان ال

# -----------

# الواحدة عشان امسك اكثر من خطأTry لل except بقدر اكتب اكثر من
# على سبيل  المثال امسك خطأ القسمة على صفر وخطأ المعرف غير موجود


try:

    print(10/0)
    # print(x)
    print(int("Hello"))
    print(3 + "d")

except ZeroDivisionError: # لأخطاء القسمة على صفر

    print("Cant Divide")

except NameError: # لاخطأ المعرف غير موجود

    print("Identifier Not Found")

except ValueError: # القيمة المدخلة خطأ

    print("Value Error Albasha")

except: # لجميع الأخطاء في حال انا مش عراف ايش نوع الخطأ

    print("Errors Happens")


# خدعة بسيطة لمعرفة نوع الخطأ اعمل الخطأ في الكود وشوف ايش اسمو في المخرجات لما يقف البرنامج ويعطيك اياه
# الخاص فيه فقط وما بكمل لبقية الأخطاء except وملاحظة ثانية لاحظ لما يمسك اول خطأ بعمل ال
# لانو مسك خطاء وخلص ليش يمر ع بقية الأخطاء

# Output

# print(10/0)           ->   Cant Divide
# print(x)              ->   Identifier Not Found
# print(int("Hello"))   ->   Value Error Albasha
# print(3 + "d")        ->   Errors Happens
