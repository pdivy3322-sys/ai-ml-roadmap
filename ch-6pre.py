a =int(input("Enter the age:"))

if (a>=18):
    print("You are abov 18th")
else:
    print("sorry,You are below 18th")
#q-1
a1 =int(input("Enter value of a1:"))
a2 =int(input("Enter value of a2:"))
a3 =int(input("Enter value of a3:"))
a4 =int(input("Enter value of a4:"))

if(a1>a2 and a1>a3 and a1>a4):
    print("a1 is gretest",a1)

elif(a2>a1 and a2>a3 and a2>a4):
    print("a2 is gretest",a2)

elif(a3>a1 and a3>a2 and a3>a4):
    print("a3 is gretest",a3)

elif(a4>a1 and a4>a2 and a4>a3):
    print("a4 is gretest",a4)
#q-2
maths=int(input("Enter value of maths:"))
SS=int(input("Enter value of ss:"))
English=int(input("Enter value of English:"))

total= (100*(maths +English +SS))/300
if(total>=40 and maths>33 and SS>33 and English>33):
    print("you are pass",total)
else:
    print("You are fail",total)
#q-3
massage1 = "Make lot of money"
massage2 = "Buy Now"
massage3 = "Subscibe Now"
massage4 = "Click Now"
massage = input("Enter Your massage")
if(massage1 in massage or massage2 in massage or massage3 in massage or massage4 in massage):
    print("massage is spam")
else:
    print("massage not spam")
#q-4
name=input("Enter username:")
if(len(name)<10):
    print("username is less then 10")
else:
    print("username is grater then 10")
#q-5
stu_name =["Rohan","Geet","Het","Ayush","Navjet"]
Name=input("Enter the Name")

if(Name in stu_name):
    print("Student is present ")
else:
    print("student is not present")
#q-6

maths = int(input("Enter value of maths: "))
SS = int(input("Enter value of ss: "))
English = int(input("Enter value of English: "))

total = (maths + English + SS) * 100 / 300
print("persentage",total)
if total <= 100 and total > 90:
    grade = "A"
elif total <= 90 and total > 80:
    grade = "B"
elif total <= 80 and total > 70:
    grade = "C"
elif total <= 70 and total > 60:
    grade = "D"
elif total <= 60 and total > 50:
    grade = "E"
else:
    grade = "Fail"

print("Your grade is:", grade)
#q-7
post=input("Enter the post")
if("Divy Patel".lower() in post.lower()):
    print("This post is talking Divy ")
else:
    print("This post is not talking about Divy")

