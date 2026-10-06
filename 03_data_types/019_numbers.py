# Lesson 019 - Numbers
# Video: https://www.youtube.com/watch?v=x7fFnKVAzDI

# -------------
# -- Numbers --
# -------------

# Integer

print(type(1))
print(type(10))
print(type(100))
print(type(-45))
print(type(-2493))

# Float

print(type(1.20))
print(type(100.5))
print(type(-10.4))
print(type(-104.4))
print(type(-2493.334))

# Complex

myComplexNumber = 5+4j

print(type(myComplexNumber))

print(f"Complex Number: {myComplexNumber}") # => Complex Number: (5+4j)
print(f"Real Part Is: {myComplexNumber.real}") # => Real Part Is: 5.0
print(f"Imaginary Part Is: {myComplexNumber.imag}") # => Imaginary Part Is: 4.0

# [1] You Can Convert From Int To Float Or Complex
# [2] You Can Convert From Float To Int Or Complex
# [3] You Cannot Convert Complex To Any Type

print(100) # => 100
print(float(100)) # => 100.0
print(complex(100)) # => (100+0j)

print (10.400) # => 10.4
print (int(10.400)) # => 10
print (complex(10.400)) # => (10.4+0j)

print(10+9j) # => (10+9j)
# print(int(10+9j)) -> Can't Convert Complex to int 
