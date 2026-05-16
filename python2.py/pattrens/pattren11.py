
n=5
for row in range(1,n+1):
    for space in range(n-row):
        print("  ",end="")
    for col in range(row):
        print("*",end=" ")
    print()
for r in range(1,n):
    for s in range(r):
        print("  ",end="")
    for c in range(n-r):
        print("*",end=" ")
    print()
