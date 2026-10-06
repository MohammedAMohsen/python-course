# Lesson 064 - Function Lambda
# Video: https://www.youtube.com/watch?v=oNp5wwu9S7c

# ------------------------
# -- Function => lambda --
# -- Anonymous Function --
# ------------------------
# [1] It Has No Name
# [2] You Can Call It Inline Without Defining It
# [3] You Can Use It In Return Data From Another Function
# [4] Lambda Used For Simple Functions and Def Handle The Large Tasks
# [5] Lambda is One Single Expression not Block Of Code
# [6] Lambda Type is Function
# -------------------------------------------------------------------

# Function => lambda is Anonymous Function => مجهولة الهوية , ملهاش إسم يعني

def say_hello(name, age): return f"Hello {name} Your Age Is: {age}"

hello = lambda name, age : f"Hello {name} Your Age Is: {age}"

print(say_hello("Mohammed", 21)) # Hello Mohammed Your Age Is: 21
print(hello("ALBasha", 21)) # Hello ALBasha Your Age Is: 21

print(say_hello.__name__) # say_hello
print(hello.__name__) # <lambda>
print(type(hello)) # <class 'function'>
