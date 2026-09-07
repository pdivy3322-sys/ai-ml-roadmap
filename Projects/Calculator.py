#To develop a simple Python calculator program that performs basic arithmetic operations such as addition, subtraction, multiplication, and division based on the user’s choice.
print("Enter the choise")
print("1.addition(+)")
print("2.subtraction(-)")
print("3.multiplication(*)")
print("4.divition(/)")
choise =(input("Enter the chosie(1,2,3,4):"))
a = int(input("Enter the 1st number"))
b = int(input("Enter the 2nd number"))
if choise =="1":
    print ("result:",a+b)
elif choise =="2":
    print("Rsult:",a-b)
elif choise =="3":
    print("Rsult:",a*b)
elif choise =="4":
    print("Rsult:",a/b)
else:
    print("your enter invalid choise")