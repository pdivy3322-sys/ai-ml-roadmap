# Q-1
# Function to print welcome message

def welcome():
    print("Welcome to Python")

welcome()


# Q-2
# Function to find average of three numbers

def avg(a, b, c):
    return (a + b + c) / 3

result = avg(1, 2, 3)

print("Average:", result)


# Q-3
# Lambda function to find square

square = lambda a: a * a

print("Square:", square(5))


# Q-4
# Lambda function to find largest number

largest = lambda a, b: a if a > b else b

print("Largest number:", largest(3, 8))


# Q-5
# Lambda function to check even or odd

check = lambda a: "even" if a % 2 == 0 else "odd"

print("Number is:", check(3))