# Lesson 054 - Loop - Break Continue Pass
# Video: https://www.youtube.com/watch?v=KtjJxOr5sp0

# ---------------------------
# -- Break, Continue, Pass --
# ---------------------------

myNumbers = [1, 2, 3, 5, 7, 10, 13, 14, 15, 19]

# Continue

for number in myNumbers:

    if number == 13:
        continue # -> أفشق عن الرقم 13 يعني ما تطبعو وكمل طباعة للي بعدو
    print(number)


# Break

for number in myNumbers:

    if number == 13:
        break # -> لما تصل للرقم 13 ما تطبعو وكمان وقف الطباعة للي بعدو
    print(number)


# Pass

for number in myNumbers:

    if number == 13:
        pass # -> بيستخدم عشان ما يطلع رسالة خطأ في حال ما كملت الكود
    print(number)
