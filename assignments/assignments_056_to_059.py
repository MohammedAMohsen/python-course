# Assignment 01

def calculate(num1, num2, operation="Add"):

    operation = operation.lower()
    if operation == "add" or operation == "a":
        return(num1 + num2)
    elif operation == "subtract" or operation == "s":
        return(num1 - num2)
    elif operation == "multiply" or operation == "m":
        return(num1 * num2)
    else:
        return("This Operation Is Not Valid")

print(calculate(10, 20)) # 30
print(calculate(10, 20, "SubTRACT")) # -10
print(calculate(10, 20, "s"))        # -10
print(calculate(10, 20, "AdD")) # 30
print(calculate(10, 20, "A"))   # 30
print(calculate(10, 20, "Multiply")) # 200
print(calculate(10, 20, "M"))        # 200
# _______________________________________________________________________________________________________
# Assignment 02

def addition(*Number):
    sum = 0
    for num in Number:
        if num == 10:
            continue
        elif num == 5:
            sum -= num
        else:
            sum += num
    return sum

print(addition(10, 20, 30, 10, 15)) # 65
print(addition(10, 20, 30, 10, 15, 5, 100)) # 160
# _______________________________________________________________________________________________________
# Assignment 03

def skills(name, *skills):
    if skills != ():
  # if skills: أو هيك تكتب
        print(f"Hello {name} Your Skills Is")
        for skill in skills:
            print(skill)
    else:
        print(f"Hello {name} You Have No Skills To Show")

skills("Albasha", "HTML", "CSS", "JS", "Python") # Hello Albasha Your Skills Is ... HTML ... CSS ... JS ... Python
skills("Mohammed") # Hello Mohammed You Have No Skills To Show
# _______________________________________________________________________________________________________
# Assignment 04

def say_hello(name = "UnKnown", age = "UnKnown", cuntry = "UnKnown"):

    return f"Hello {name} Your Age Is {age} And You Live In {cuntry}"

print(say_hello("Mohammed", 21, "Gaza")) # Hello Mohammed Your Age Is 21 And You Live In Gaza
print(say_hello("Mohammed", 21)) # Hello Mohammed Your Age Is 21 And You Live In UnKnown
print(say_hello("Mohammed",)) # Hello Mohammed Your Age Is UnKnown And You Live In UnKnown
print(say_hello()) # Hello UnKnown Your Age Is UnKnown And You Live In UnKnown