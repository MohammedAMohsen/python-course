# Lesson 020 - Arithmetic Operators
# Video: https://www.youtube.com/watch?v=prv7cVm2dxE

# --------------------------
# -- Arithmetic Operators --
# --------------------------
# [+] Addition
# [-] Subtraction
# [*] Multiplication
# [/] Division
# [%] Modulus
# [**] Exponent
# [//] Floor Division
# --------------------------

# Addition [+]

print(10 + 44) 
print(-10 + 44)
print(1 + 2.55)
print(1.3 + 1.4)

# Subtraction [-]

print(10 - 44) 
print(-10 - 44)
print(-1 - -2.55) # => 1.5499999999999998
print(1.3 - 1.4)  # => -0.09999999999999987
# لماذا لم يظهر الناتج 1.55 بالضبط؟
# الحاسوب يخزن الأعداد العشرية بشكل تقريبي، فيظهر فرق صغير جداً في آخر الرقم
# هذا طبيعي في كل لغات البرمجة، وللتقريب نستخدم الدالة التالية
# round(1.5499999999999998, 2) => 1.55

# Multiplication [*]

print(10 * 44) 
print(-10 * 44)
print(5 + 10 * 100)   # => 1005 --> الإفتراضي أنو بضرب بالأول لأنو الضرب أقوى من الجمع
print((5 + 10) * 100) # => 1500 --> هان جمع لأنو الأقواس أقوى من الضرب

# Division [/]

print(100/20) # => 5.0
print(int(100/20)) # => 5

# Modulus [%]

print(8%2) # => 0
print(9%2) # => 1
print(20%5) # => 0
print(22%5) # => 2

# Exponent [**]

print(10**2) # => 10 * 10 = 100
print(5**3) # => 5 * 5 * 5 = 125

# Floor Division [//] 

print(100 // 20) # => 5
print(110 // 20) # => 5
print(115 // 20) # => 5
print(119 // 20) # => 5
print(120 // 20) # => 6
print(130 // 20) # => 6
print(139 // 20) # => 6
print(140 // 20) # => 7
print(155 // 20) # => 7

