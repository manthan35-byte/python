"""
nested if statement:

when if condition call inside the another if statement 
its called nested if statement 

syntax:
if condition:
    if condition:
        statement
    else:
        statement
else:
    if condition:
        statement
    else:
        statement

"""
marks =int(input("enter your marks:"))
if marks>= 0 and marks <= 100:
    if marks >= 70:
        print("A grade")
    elif marks >=60 and marks <=70:
        print("B grade")
    elif marks >=50 and marks <=60:
        print("c grade")
    elif marks >=40 and marks <=50:
        print("D grade")
    else:
        print("fail")
else:
    print("invalid marks")

