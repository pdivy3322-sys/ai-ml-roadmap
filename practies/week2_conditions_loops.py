# Q-1
# Check age

age = int(input("Enter the age: "))

if age >= 18:
    if age >= 60:
        print("The person is Senior Citizen")
    else:
        print("The person is Adult")
else:
    print("The person is Minor")


# Q-2
# Username and password

username = input("Enter your Username: ")
password = int(input("Enter the password: "))

if username == "admin":
    if password == 1234:
        print("Login successfully")
    else:
        print("Wrong password")
else:
    print("Wrong Username")


# Q-3
# Check positive even or odd

num = int(input("Enter the number: "))

if num > 0:
    if num % 2 == 0:
        print("Positive even:", num)
    else:
        print("Positive odd:", num)
else:
    print("Number is zero")


# Q-4
# Print numbers from 1 to 10

i = 1

while i <= 10:
    print("Number:", i)
    i += 1


# Q-5
# Print numbers from 1 to 100

i = 1

while i <= 100:
    print(i)
    i += 1


# Print even numbers from 1 to 20

i = 1

while i <= 20:
    if i % 2 == 0:
        print("Even:", i)
    i += 1


# Print odd numbers from 1 to 20

i = 1

while i <= 20:
    if i % 2 != 0:
        print("Odd:", i)
    i += 1


# Multiplication table using while loop

a = int(input("Enter the number: "))

i = 1

while i <= 10:
    print(a, "*", i, "=", i * a)
    i += 1


# Q-8
# Sum of numbers from 1 to n

n = int(input("Enter the number: "))

i = 1
sum = 0

while i <= n:
    sum = sum + i
    i += 1

print("Final sum:", sum)


# Q-9
# Count digits

n = int(input("Enter the number: "))

count = 0

while n > 0:
    count += 1
    n = n // 10

print("Number of digits:", count)


# Continue and break

a = int(input("Enter the number: "))

i = 1

while i <= a:
    if i == 4:
        i += 1
        continue

    print(i)
    i += 1


# Check even and odd numbers

i = 1

while i <= 20:
    if i % 2 == 0:
        print(i, "even")
    else:
        print(i, "odd")

    i += 1


# Ask number until user enters zero

while True:
    a = int(input("Enter the number: "))

    if a != 0:
        print("Try again")
    else:
        break

print("The user entered zero")


# Password checking

while True:
    password = int(input("Enter the password: "))

    if password == 1234:
        print("Login successful")
        break
    else:
        print("Try again")


# Multiplication table using for loop

a = int(input("Enter the number: "))

for i in range(1, 11):
    b = i * a
    print(a, "*", i, "=", b)


# Fizz program

a = int(input("Enter the value: "))

for i in range(1, 10):
    if i % a == 0:
        print("Fizz")
    else:
        print(i)


# Sum of odd numbers from 1 to 20

sum = 0

for i in range(1, 21):
    if i % 2 != 0:
        sum = sum + i

print("Sum of odd numbers:", sum)


# Skip 10 and 15

for i in range(1, 20):
    if i == 10 or i == 15:
        continue

    print(i)


# Print even numbers from 0 to 20

for i in range(0, 21, 2):
    print("Even:", i)


# Print odd numbers from 1 to 20

for i in range(1, 21, 2):
    print("Odd:", i)


# Nested loop

for i in range(1, 3):
    for j in range(1, 3):
        print(i, j)


# Increasing star pattern

for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()


# Decreasing star pattern

for i in range(5, 0, -1):
    for j in range(i):
        print("*", end="")
    print()


# Increasing and decreasing star pattern

for i in range(1, 5):
    for j in range(i):
        print("*", end="")
    print()

for i in range(4, 0, -1):
    for j in range(i):
        print("*", end="")
    print()


# Right triangle pattern

for i in range(1, 6):
    for j in range(5 - i):
        print(" ", end="")

    for k in range(i):
        print("*", end="")

    print()


# Right triangle pattern

for i in range(1, 6):
    for j in range(5 - i):
        print(" ", end="")

    for k in range(i):
        print("*", end="")

    print()


# Pyramid pattern

for i in range(1, 6):
    for j in range(5 - i):
        print(" ", end="")

    for k in range(2 * i - 1):
        print("*", end="")

    print()


# Reverse pyramid pattern

for i in range(5, 0, -1):
    for j in range(5 - i):
        print(" ", end="")

    for k in range(2 * i - 1):
        print("*", end="")

    print()


# Print each character of name

name = input("Enter the Name: ")

for i in name:
    print("Character:", i)


# Print vowels from name

name = input("Enter the name: ")

for i in name:
    if i in "aeiou":
        print("Vowel:", i)


# Count consonants

name = input("Enter the name: ")

count = 0

for i in name:
    if i not in "aeiou":
        count = count + 1
        print("Consonant:", i)

print("Total consonants:", count)


# Count a particular character

name = input("Enter the Name: ")
char = input("Enter the char you want: ")

count = 0

for i in name:
    if i == char:
        count += 1

print("Character count:", count)

# Q-1
# Check positive, negative, even or odd

a = int(input("Enter the number: "))

if a > 0:
    if a % 2 == 0:
        print("Positive even")
    else:
        print("Positive odd")

elif a < 0:
    if a % 2 == 0:
        print("Negative even")
    else:
        print("Negative odd")

else:
    print("Zero")


# Q-3
# Print numbers divisible by 3

n = int(input("Enter the number: "))

for i in range(1, n):
    if i % 3 == 0:
        print("Divisible by 3:", i)


# Q-4
# Sum and count of even numbers

a = int(input("Enter the number: "))

count = 0
sum = 0

for i in range(1, a + 1):
    if i % 2 == 0:
        sum = sum + i
        count = count + 1

print("Sum =", sum)
print("Count =", count)


# Q-5
# Star pattern

for i in range(1, 5):
    for j in range(i):
        print("*", end="")
    print()

for i in range(4, 0, -1):
    for j in range(i):
        print("*", end="")
    print()


# Count vowels and consonants

name = input("Enter the name: ")

count = 0
voll = 0

for i in name:
    if i in "aeiou":
        voll = voll + 1
    elif i.isalpha():
        count = count + 1

print("Total vowels:", voll)
print("Total consonants:", count)