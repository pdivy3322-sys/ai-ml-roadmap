# Q-1
# Different data types

a = 20
print(a)
print(type(a))

b = 25.8
print(b)
print(type(b))

c = "THIS VARIABLE TYPE"
print(c)
print(type(c))

D = True
print(D)
print(type(D))

E = [12, 13, 14, 15]
print(E)
print(type(E))

f = (12, 13, 14)
print(f)
print(type(f))

g = {
    "da1": "12",
    "db2": "chatgpt"
}
print(g)
print(type(g))

h = {1, 2, 3, 4, 1, 2, 3}
print(h)
print(type(h))

m = input("Enter the number: ")
print(m)


# Q-2
# Addition of two numbers

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print("Addition =", a + b)


# Q-3
# Multiplication of two numbers

c = int(input("Enter the first number: "))
d = int(input("Enter the second number: "))

print("Multiplication =", c * d)


# Q-4
# Area of circle

a = float(input("Enter the radius: "))

b = 3.14 * a * a

print("Area of circle =", b)


# Q-5
# Celsius to Fahrenheit

a = float(input("Enter the Celsius: "))

b = a * 9 / 5 + 32

print("Fahrenheit =", b)


# Q-6
# Average of three numbers

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))

d = (a + b + c) / 3

print("Average =", d)


# Q-7
# Find remainder

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

print("Remainder =", a % b)


# Q-8
# Check even or odd

a = int(input("Enter the number: "))

if a % 2 == 0:
    print("The number is even", a)
else:
    print("The number is odd", a)


# Q-9
# Find largest of two numbers

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if a > b:
    print("The largest number is", a)
elif a < b:
    print("The largest number is", b)
else:
    print("Both numbers are equal")


# Q-10
# Check positive, negative or zero

a = int(input("Enter the number: "))

if a > 0:
    print("The number is positive")
elif a < 0:
    print("The number is negative")
else:
    print("The number is zero")


# Q-11
# Check divisible by 5

a = int(input("Enter the number: "))

if a % 5 == 0:
    print("The number is divisible by 5", a)
else:
    print("The number is not divisible by 5", a)


# Q-12
# Simple calculator

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
op = input("Enter the operator: ")

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    print(a / b)
else:
    print("Invalid operator")


# Q-13
# Check leap year

a = int(input("Enter the year: "))

if a % 4 == 0:
    print("This is a leap year")
else:
    print("This is not a leap year")


# Q-14
# Find largest of three numbers

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if a >= b and a >= c:
    print("The largest number is", a)
elif b >= a and b >= c:
    print("The largest number is", b)
else:
    print("The largest number is", c)


# Q-15
# Multiplication table

a = int(input("Enter the number: "))

for i in range(0, 11):
    print(a, "*", i, "=", a * i)


# Q-16
# Sum of numbers from 1 to n

a = int(input("Enter the number: "))

sum = 0

for i in range(1, a + 1):
    sum = sum + i

print("Final sum:", sum)