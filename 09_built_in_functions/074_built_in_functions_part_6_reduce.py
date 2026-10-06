# Lesson 074 - Built In Functions Part 6 Reduce
# Video: https://www.youtube.com/watch?v=bgV0RHfRhB4

# ----------------------------------
# -- Built In Functions => Reduce --
# ----------------------------------
# [1] Reduce Take A Function + Iterator
# [2] Reduce Run A Function On First and Second Element And Give Result
# [3] Then Run Function On Result And Third Element
# [4] Then Run Function On Result And Fourth Element And So On
# [5] Till One ELement is Left And This is The Result of The Reduce
# [6] The Function Can Be Pre-Defined Function or Lambda Function
# [7] بسبب التحديثات الجديدة على اللغة Import طريقة الإستدعاء عن طريق 
# ---------------------------------------------------------------

# :ببساطة تشبه الفلتر والماب ولكن الفرق انها بتاخذ القيم وبطبق عليهم التالي
# بتاخذ او عنصرين وعلى سبيل المثال بتجمعهم والناتج بتجمعو مع العنصر الثالث والناتح بتجمعو مع العنصر الرابع وهكذا
# calculates ((((1 + 2) + 3) + 4) + 5).

from functools import reduce

# Example 1:

def sumAll(num1, num2):

    return num1 + num2

number = [1, 8, 2, 9, 100]

result = reduce(sumAll, number)

print(result) # ((((1 + 8) + 2) + 9) + 100) = 120

# Example 2: With Lambda:

print(reduce(lambda x, y: x+y, number)) # 120
