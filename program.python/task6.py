posi=0
negi=0
for i in range(1,6):
    num=int(input(f"enter number {i}:"))
    if num>0:
        print("number is positive")
        posi+=1
    else:
        print("number is negative")
        negi+=1