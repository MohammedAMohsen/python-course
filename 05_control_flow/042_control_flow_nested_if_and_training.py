# Lesson 042 - Control Flow - Nested If And Training
# Video: https://www.youtube.com/watch?v=W6KsrqVvg2E

# ---------------
# -- Nested If --
# ---------------

uName = "Mohammed"
isStudent = "Yes"
uCountry = "KSA"
# uCountry = "Gaza"
# uCountry = "Kuwait"
# uCountry = "Egypt"
# uCountry = "Bahrain"
cName = "Python Course"
cPrice = 100


if uCountry == "Gaza" or uCountry == "KSA" or uCountry == "Qatar" :
    
    if isStudent == "Yes" :

        print(f"Hello {uName} Because You Are From {uCountry} And Student") # Hello Mohammed Because You Are From KSA And Student
        print(f"The Course \"{cName}\" Price Is: ${cPrice - 90}") # The Course "Python Course" Price Is: $10

    else :

        print(f"Hello {uName} Because You Are From {uCountry}") # Hello Mohammed Because You Are From Gaza Or KSA
        print(f"The Course \"{cName}\" Price Is: ${cPrice - 80}") # The Course "Python Course" Price Is: $20

elif uCountry == "Kuwait" or uCountry == "Bahrain": 

    print(f"Hello {uName} Because You Are From {uCountry}") # Hello Mohammed Because You Are From Kuwait or Bahrain
    print(f"The Course \"{cName}\" Price Is: ${cPrice - 50}") # The Course "Python Course" Price Is: $50

else : 

    print(f"Hello {uName} Because You Are From {uCountry}") # Hello Mohammed Because You Are From Egypt
    print(f"The Course \"{cName}\" Price Is: ${cPrice - 30}") # The Course "Python Course" Price Is: $70
