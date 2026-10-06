# Lesson 041 - Control Flow - If, Elif, Else
# Video: https://www.youtube.com/watch?v=v8ZehXS3XF0

# --------------------
# --  Control Flow  --
# -- If, Elif, Else --
# -- Make Decisions --
# --------------------

uName = "Mohammed"
# uCountry = "Gaza"
# uCountry = "Kuwait"
# uCountry = "KSA"
uCountry = "Egypt"
cName = "Python Course"
cPrice = 100


if uCountry == "Gaza" :

    print(f"Hello {uName} Because You Are From {uCountry}") # Hello Mohammed Because You Are From Gaza
    print(f"The Course \"{cName}\" Price Is: ${cPrice - 80}") # The Course "Python Course" Price Is: $20

elif uCountry == "KSA" : 

    print(f"Hello {uName} Because You Are From {uCountry}") # Hello Mohammed Because You Are From KSA
    print(f"The Course \"{cName}\" Price Is: ${cPrice - 64}") # The Course "Python Course" Price Is: $36

elif uCountry == "Egypt" : 

    print(f"Hello {uName} Because You Are From {uCountry}") # Hello Mohammed Because You Are From Egypt
    print(f"The Course \"{cName}\" Price Is: ${cPrice - 40}") # The Course "Python Course" Price Is: $60

else : 

    print(f"Hello {uName} Because You Are From {uCountry}") # Hello Mohammed Because You Are From Kuwait
    print(f"The Course \"{cName}\" Price Is: ${cPrice - 30}") # The Course "Python Course" Price Is: $70
