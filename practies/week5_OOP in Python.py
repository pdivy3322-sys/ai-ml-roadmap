"""
PYTHON OBJECT-ORIENTED PROGRAMMING (OOP)
Week 5: OOP Practicals

Description:
This file contains practical programs to understand
classes, objects, methods, constructors, encapsulation,
and inheritance in Python.
"""


# ============================================================
#                    1. CLASS AND OBJECT
# ============================================================


# Program 1: Create a Student Class
# Aim: To create a class, instantiate an object, and call a method.

class Student:
    def display(self):
        print("This is a student")


s1 = Student()
s1.display()


# Program 2: Create a Car Class
# Aim: To create a Car class and display a message using its method.

class Car:
    def start(self):
        print("Car is starting")


c1 = Car()
c1.start()


# ============================================================
#                  2. METHODS AND ATTRIBUTES
# ============================================================


# Program 3: Display Student Details using a Method
# Aim: To pass arguments to a method and store them as attributes.

class Student:
    def display(self, name, age):
        self.name = name
        self.age = age

        print("Name:", self.name)
        print("Age:", self.age)


s1 = Student()
s1.display("Rahul", 10)


# Program 4: Initialize Student Details using Constructor
# Aim: To initialize object attributes using the __init__() method.

class Student:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


s1 = Student(10, "Rahul")
s1.display()


# ============================================================
#                    3. CONSTRUCTOR
# ============================================================


# Program 5: Calculate Student Average Marks
# Aim: To initialize student data and calculate average marks.

class Student:
    def __init__(self, marks, name):
        self.name = name
        self.marks = marks

    def average(self):
        total = 0

        for mark in self.marks:
            total += mark

        if len(self.marks) > 0:
            avg = total / len(self.marks)
            print(self.name, "Average is", avg)
        else:
            print("No marks available")


s1 = Student([90, 89, 96], "Rahul")
s1.average()


# ============================================================
#                    4. CLASS METHODS
# ============================================================


# Program 6: Create a Calculator Class
# Aim: To perform arithmetic operations using class methods.

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        print("Addition:", self.num1 + self.num2)

    def sub(self):
        print("Subtraction:", self.num1 - self.num2)

    def mul(self):
        print("Multiplication:", self.num1 * self.num2)

    def div(self):
        if self.num2 != 0:
            print("Division:", self.num1 / self.num2)
        else:
            print("Division by zero is not allowed")


c1 = Calculator(10, 5)
c1.add()
c1.sub()
c1.mul()
c1.div()


# Program 7: Display Employee Details
# Aim: To store and display employee name and salary using a class.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)


e1 = Employee("Rahul", 25000)
e1.display()


# ============================================================
#                      5. INHERITANCE
# ============================================================


# Program 8: Single Inheritance
# Aim: To inherit a method from a parent class into a child class.

class Animal:
    def eat(self):
        print("Animal is eating")


class Dog(Animal):
    pass


d1 = Dog()
d1.eat()


# Program 9: Method Overriding
# Aim: To override a parent class method in a child class.

class Vehicle:
    def start(self):
        print("Vehicle is starting")


class Bike(Vehicle):
    def start(self):
        print("Bike is starting")


b1 = Bike()
b1.start()


# Program 10: Use super() in Method Overriding
# Aim: To call the parent class method using super() and
# then execute the child class method.

class Vehicle:
    def start(self):
        print("Vehicle is starting")


class Bike(Vehicle):
    def start(self):
        super().start()
        print("Bike is starting")


b1 = Bike()
b1.start()


# ============================================================
#                      END OF FILE
# ============================================================