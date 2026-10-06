# Lesson 043 - Control Flow - Ternary Conditional Operator
# Video: https://www.youtube.com/watch?v=1E7z7r61b2s

# ----------------------------------
# -- Ternary Conditional Operator --
# ----------------------------------

country = "Egypt"

if country == "Egypt" : print(f"The Weather in {country} Is 15") # The Weather in Egypt Is 15

elif country == "KSA" : print(f"The Weather in {country} Is 30")

else : print("Country is Not in The List")

# Short If => Condition If True | If Condition | Else | Condition If False

movieRate = 18
age = 19

if age < movieRate :
    print("Movie S Not Good 4U :(") # Condition If True
else :
    print("Movie S Good 4U And Happy Watching :)") # Condition If False

print("Movie S Not Good 4U :(" if age < movieRate else "Movie S Good 4U And Happy Watching :)") # This is Short If (إختصار)
