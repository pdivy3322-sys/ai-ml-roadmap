# class Student:
#     def display(self):
#         print("This is a student")

# s1 = Student()
# s1.display()

# class car:
#     def start(self):
#         print("car is starting")
# c1 = car()
# c1.start()

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def get_ave(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("Hello", self.name, "your average is", sum / 3)

# s1 = Student("John", [90, 89, 96])
# s1.get_ave()
# p=1
# class car:
#     def start(self):
#         print("car is starting ")
# c1=car()
# c1.start()
# p=2
# class student:
#     def display(self , name,age):
#         self.name = name
#         self.age = age
#         print("Name is",self.name)
#         print("Age is",self.age)
# c1 = student()
# c1.display("rau",10)
# #p=3
# class student:
#     def __init__(self,age,name):
#         self.age = age
#         self.name = name
#     def display(self):
#         print("Name is",self.name)
#         print("Age is",self.age)
# c1 = student(10,"rau")
# c1.display()
# p=4
# class student:
#     def __init__(self,marks,name):
#        self.name = name
#        self.marks = marks
#     def average(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print(self.name,"Average is",sum/3)
# c1 = student([90,89,96],"Rahul")
# c1.average()
# p=5
# class calculator:
#     def __init__(self,num1,num2):
#         self.num1 = num1
#         self.num2 = num2
#     def add(self):
#         print("Addition is",self.num1+self.num2)
#     def sub(self):
#         print("Subtraction is",self.num1-self.num2)
#     def mul(self):
#         print("Multiplication is ",self.num1*self.num2)
#     def div(self):
#         print("division is ",self.num1/self.num2)
# c1 = calculator(10,5)
# c1.add()
# c1.sub()
# c1.mul()
# c1.div()
# p=6
# class emp:
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary
#     def display(self):
#         print("name is ",self.name)
#         print("salary is ",self.salary)
# c1 = emp("Rahul",25000)
# c1.display()
# p=7
# class animal:
#     def eat(self):
#         print("Animal is eating")
#     def dog(animal):
#         pass
# c1 = animal()
# c1.eat()
# class vehicle:
#     def start(self):
#         print("vehical is staring ")
# class bike(vehicle):
#     def start(self):
#         print("bike is staring")
# d1 = bike()
# d1.start()
# class vehicle:
#     def start(self):
#         print("vehical is staring ")
# class bike(vehicle):
#     def start(self):
#         super().start()
#         print("bike is staring")
# d1 = bike()
# d1.start()