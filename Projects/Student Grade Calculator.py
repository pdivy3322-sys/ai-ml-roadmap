# To develop a Python program using a function to accept a student's marks, validate the marks, and determine the appropriate grade or pass/fail status based on the given marks.
def cla(mark):
    if mark >100 or mark <0:
        grade = "The marks is invalid "
    elif mark >=90:
        grade="Grade A"
    elif mark >=80:
        grade="Grade B"
    elif mark>=70:
        grade = "Grade C"
    elif mark >=60:
        grade = "Gread D"
    elif mark >=50:
        grade="Grade E"
    elif mark >=45:
        grade="You are pass"
    else :
        grade = "Fail, try next year"
    return grade
mark = int(input("Enter the Marks:"))
result = cla(mark)
print(result)