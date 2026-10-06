# Assignment 01

NUM = input("Add Your Number: ")

if len(NUM) > 1:
   
   raise IndexError("Only One Character Allowed")

elif NUM == "0":
   
   raise ValueError("Number Must Be Larger Than 0")

elif NUM.isdigit():

   print(f"The Number Is {NUM}")

else:
      
     raise Exception("Only Numbers Allowed")

# _______________________________________________________________________________________________________
# Assignment 02

LETTER = input("Add Letter From A to Z: ")

try:
     if len(LETTER) > 1:
          
          raise IndexError()
     
     elif not LETTER.isupper():
          
          raise TypeError()
     
except IndexError:
     
     print("You Must Write One Character Only")

except TypeError:
     
     print("The Letter Not In A - Z")

else:
     
     print(f"You Typed {LETTER}")
# _______________________________________________________________________________________________________
# Assignment 03

def calculate(num1, num2) -> int:
  return num1 + num2

print(calculate(20, 30))