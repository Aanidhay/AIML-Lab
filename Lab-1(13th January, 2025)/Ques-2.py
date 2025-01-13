#Create variables of diff datatypes and perform basic operations on them

integer=10
float=50
string="Hello"
boolean=True

#Performing arithmetic operations on numeric data types

addition = integer+float
subtraction =integer-float
multiplication =integer*float
division =integer/float
modulus =integer%float

print(f"addition:{integer}+{float}={addition}")
print(f"subtraction:{integer}-{float}={subtraction}")
print(f"multiplication:{integer}*{float}={multiplication}")
print(f"division:{integer}/{float}={division}")
print(f"modulus:{integer}%{float}={modulus}")

concatenated_string=string+"World!!"
print(concatenated_string)

andop = boolean and False
orop = boolean or False
notop = not boolean
print(andop)
print(orop)
print(notop)