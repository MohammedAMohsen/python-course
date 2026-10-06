# Lesson 051 - Loop For and Else
# Video: https://www.youtube.com/watch?v=4YolrVX6f1Q

# -----------------
# -- Loop => For --
# -----------------
# for item in iterable_object :
#   Do Something With Item
# -----------------------------
# item Is A Variable You Create and Call Whenever You Want
# item refer to the current position and will run and visit all items to the end
# iterable_object => Sequence [ list, tuples, set, dict, string of characters, etc ... ]
# ---------------------------------------------------------------

myNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# for number in myNumbers:

#     print(number)

for number in myNumbers:

    if number % 2 == 0: # Even

        print(f"The Number {number} Is Even.")

    else:

        print(f"The Number {number} Is Odd.")

else: # ->  elseانها لو ما تنفذ الشرط إدخل على ال While تعت elseعادي, بختلف عن ال elseهان بعد ما يخلص بدخل على ال

    print("The Loop Is Finished")


myName = "Mohammed"

for letter in myName:

    print(letter.upper())

# M
# O
# H
# A
# M
# M
# E
# D
