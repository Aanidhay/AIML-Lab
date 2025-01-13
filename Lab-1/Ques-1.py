#Write a Python program to perform basic arithmetic operations(addition,subtraction,multiplication,division and modulus) on 2 numbers

num1 = float(input("Enter the num 1: "))
num2 = float(input("Enter the num 2: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
modulus = num1 % num2

print(f"addition: {num1} + {num2} = {addition}")
print(f"Subtraction: {num1} - {num2} = {subtraction}")
print(f"Multiplication: {num1} * {num2} = {multiplication}")
print(f"Division: {num1} / {num2} = {division}")
print(f"Modulus: {num1} % {num2} = {modulus}")