# Lesson 129 - Advanced Lessons - Timing Your Code With Timeit
# Video: https://www.youtube.com/watch?v=4tKWqrBiLjo

# ------------------------------------------------------
# -- Advanced_Lessons => Timing Your Code With Timeit --
# ------------------------------------------------------
# - timeit: - Get Execution Time Of Code By Running It 1M Times And Give You The Total Time
# -         - It Used For Performance By Testing All Functionality
# - timeit(stmt, setup, timer, number)
# - timeit(pass, pass, default, 1.000.000) Default Values
# -------------------------------------------------------
# - stmt: Code You Want To Measure The Execution Time
# - setup: Setup Done Before The Code Execution (Import Module Or Anything)
# - timer: The Timer Value
# - number: How Many Execution That Will Run
# -------------------------------------------------------

import timeit

# print(dir(timeit)) 

# هينفذ العملية التالية مليون مرة ويرجعلي مجموع الوقت كله بالثواني
# ملاحظة: الأرقام في هذا الدرس تختلف حسب سرعة جهازك وفي كل تشغيل

print(timeit.timeit("'Albasha' * 1000")) # 0.3825277409996488

# Name = "Alabsha"
# print(Name * 1000)

print(timeit.timeit("name = 'Albasha'; name * 1000")) # 0.3825277409996488

# print(random.randint(0, 50)) # 23

print(timeit.timeit(stmt="random.randint(0, 50)", setup="import random")) # 0.7036368049994053

# هن بعمل العملية الي بتعمل مليون مرة أربع مرات وبيعطيني نتائج الأربع مرات كل مرة على حدى في قائمة

print(timeit.repeat(stmt="random.randint(0, 50)", setup="import random", repeat=4)) 

# [0.8695622419982101, 0.8804346079996321, 0.8353255869988061, 0.9164055359979102]

# أقل رقم في القائمة هو الأدق، لأن الأرقام الأكبر تأثرت ببرامج أخرى تعمل على الجهاز
# print(min(timeit.repeat(stmt="random.randint(0, 50)", setup="import random", repeat=4)))

