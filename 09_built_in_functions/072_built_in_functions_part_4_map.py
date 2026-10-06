# Lesson 072 - Built In Functions Part 4 Map
# Video: https://www.youtube.com/watch?v=JvbLI0z8t8c

# -------------------------------
# -- Built In Functions => Map --
# -------------------------------
# [1] Map Take A Function + Iterator
# [2] Map Called Map Because It Map The Function On Every Element
# [3] The Function Can Be Pre-Defined Function or Lambda Function
# ---------------------------------------------------------------

# Use Map With Predefined Function

def formatText(text):
    return f"- {text.strip().capitalize()} -"

myText = [" MoHMmed ", "AHMed", "Sayed "]

# -------------- map(function, iterable) -------------

myFormatedDate = map(formatText, myText)

for name in myFormatedDate:
    print(name)

# ------------- ممكن تكتب بدون تعريف -------------

for name in map(formatText, myText):
    print(name)

# ----------- list() او ممكن توضع داخل ------------

for name in list(map(formatText, myText)):
    print(name)


# Use Map With Lambda Function

for name in list(map(lambda text: f"- {text.strip().capitalize()} -", myText)):
    print(name)
