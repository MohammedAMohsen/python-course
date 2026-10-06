# Lesson 063 - Function Recursion
# Video: https://www.youtube.com/watch?v=zFVdMyr6CIo

# ------------------------
# -- Function Recursion --> فنقشن بتنادي نفسها جو نفسها وبتنادي نفسها جو نفسها وهكذا
# ------------------------
# ---------------------------------------------------------------------
# -- To Understand Recursion, You Need to First Understand Recursion --
# ---------------------------------------------------------------------

# cleanWord Word [ WWWoooorrrldd ] # print(x[1:]) -> WWoooorrrldd

def cleanWord(word):

    if len(word) == 1:

        return word

    if word[0] == word[1]: # WWWoooorrrldd / WWoooorrrldd / Woooorrrldd / oooorrrldd / ooorrrldd / oorrrldd / orrrldd / rrrldd ....
        # لحد ما تصل إنو ما بساوية Functionهل العنصر الأول بساوي العنصر الى بعدو , اذا أه عاود إرجع وكرر ال

        print(f" if - {word}") # عشان نفهم العملية هطبع الناتج حبة حبة

        return cleanWord(word[1:])

    else: # -> من بعد بواحد وعاود شغلها وأفحص العناصر functionفي حال ما كان أول عنصر بساوي ثاني عنصر رجع أول عنصر وزود على 

        print(f" re - {word}") # عشان نفهم العملية هطبع الناتج حبة حبة

        return word[0] + cleanWord(word[1:]) #  W + o + r + l + d

    # stash [ World ]

print(cleanWord("WWWoooorrrldd"))

#  if - WWWoooorrrldd
#  if - WWoooorrrldd
#  re - Woooorrrldd
#  if - oooorrrldd
#  if - ooorrrldd
#  if - oorrrldd
#  re - orrrldd
#  if - rrrldd
#  if - rrldd
#  re - rldd
#  re - ldd
#  if - dd
# World

# الطريقة بدون اضافات او تعليقات

def cleanWord(word):
    if len(word) == 1:
        return word
    if word[0] == word[1]:
        return cleanWord(word[1:])
    return word[0] + cleanWord(word[1:])

print(cleanWord("mmmoohaammmmmeed"))
