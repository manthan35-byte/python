"""
count no. of even nos and count no. of odd nos
"""

e_count = 0
o_count = 0

for i in range(1,6):
    num = int(input("Enter a number : "))

    if num % 2 == 0:
        e_count += 1
    else:
        o_count += 1

print(f"total even nos are : {e_count}")
print(f"total odd nos are : {o_count}")
