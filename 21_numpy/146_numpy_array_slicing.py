# Lesson 146 - Numpy - Array Slicing
# Video: https://www.youtube.com/watch?v=EJ_TW1qiFI0

# ----------------------------
# -- Numpy => Array Slicing --
# ----------------------------

import numpy as np

# Slising => [Start:End:Steps] Not Including End

a = np.array(["A", "B", "C", "D", "E", "F"])

print(a.ndim) # 1
print(a[1]) # B
print(a[1:4]) # ['B' 'C' 'D']
print(a[:4]) # ['A' 'B' 'C' 'D']
print(a[2:]) # ['C' 'D' 'E' 'F']

a = np.array([ ["A", "B", "Z"], ["C", "D", "X"], ["E", "F", "C"] ])

print(a.ndim) # 2
print(a[1][1]) # D
print(a[0:2]) # [ ['A' 'B' 'Z'] ['C' 'D' 'X'] ]
print(a[0:2, 0:2]) # [ ['A' 'B'] ['C' 'D'] ]
print(a[-2:, -2:]) # [ ['D' 'X'] ['F' 'C'] ]
print(a[-2:, -2::2]) # [ ['D'] ['F'] ]
print(a[-1:, -2:]) # [['F' 'C']] -> النتيجة ما زالت ثنائية الأبعاد لأننا استخدمنا التقطيع

