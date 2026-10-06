# Lesson 008 - Variables Part Two
# Video: https://www.youtube.com/watch?v=U0307lBCiDk

# ------------------------------------------------------------
# ---------------
# -- Variables --
# ---------------
# Source Code : Original Code You Write it in Computer
# Translation : Converting Source Code Into Machine Language
# Compilation : Translate Code Before Run Time
# Run-Time    : Period App Take To Executing Commands
# Interpreted : Code Translated On The Fly During Execution
# ------------------------------------------------------------

x = 10
x = "Hello"
print(x) # Hello => بدون مشاكل وهيا شغالة xاللغة قامت بتغيير القيمة لل

# print = 55
# print(print) ERROR => TypeError: 'int' object is not callable
# كلمة print ليست كلمة محجوزة، هي دالة جاهزة في اللغة
# اللغة تسمح لك أن تعطيها قيمة جديدة، لكن الدالة الأصلية تضيع ولا تعود تعمل
# لذلك لا تستخدم أسماء الدوال الجاهزة كأسماء للمتغيرات

# Reserved Words
# help("keywords") # طريقة معرفة الكلمات المحجوزة
# الكلمة يجب أن تكون بأحرف صغيرة، لأن اللغة حساسة لحالة الأحرف

a, b, c = 1, 2, 3  # تعيين قيم لمتغيرات دفعة واحدة مع بعض
print(a)
print(b)
print(c)
