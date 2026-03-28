"""
format function or format string
"""
num=int(input("enter your num :"))
name=input("enter your name :")

"""
expected output : your name is ___ and your num is ___
"""

print("your name is ",name,"your num is",num)

print(f"your name is {name} and your num is {num}")

n1= int(input("enter number 1 :"))
n2= int(input("enter number 2 :"))

ans=n1+n2
print(f"{n1} + {n2} = {ans}")

print("{2} = {0} + {1}".format(n1,n2,ans))
