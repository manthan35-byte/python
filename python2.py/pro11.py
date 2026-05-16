"""
elif statement :
    when we want to apply multiple condition we can use elif statement

syntax : 
if condition:
    statement
elif condition:
    statement
else:
    statement
"""
marks =int(input("enter your marks:"))
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
 
