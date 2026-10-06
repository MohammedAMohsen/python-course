# Lesson 007 - Variables Part One
# Video: https://www.youtube.com/watch?v=hQnZxqp3Q0Y

# --------------------------------------------------------
# -- Variables --
# ---------------
# Syntax => [Variable Name] [Assignment Operator] [Value]
#
# Name Convention and Rules
# [1] Can Start With (a-z A-Z) Or Underscore
# [2] You Cannot Start With Num Or Special Characters
# [3] Can Include (0-9) Or Underscore
# [4] Cannot Include Special Characters
# [5] Name is Not Like name [ Case Sensitive ]
# --------------------------------------------------------

myVariable = "My Value"
# _myVariable = "My Value"  => صح
# my_Variable = "My Value"  => صح
# my55Variable = "My Value" => صح
print(myVariable)

name = "Mohammed Mohsen"  # Single Word => Normal
myName = "Mohammed Mohsen"  # Two Words => camelCase
my_name = "Mohammed Mohsen"  # Two Words => snake_case
print(name,myName,my_name)

Good = "Good1"   
good = "Good2"  # يختلف عن المتغير الي قبلو لانو اللغة حساسة لحالة الأحرف
print(Good)
print(good)
