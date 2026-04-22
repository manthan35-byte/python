print("clothing store billing system")


name=input("enter ur name:")
item=input("clothing items:")
price=int(input("enter ur price:"))
quantity=int(input("quantity of items:"))

total=price * quantity
dicsount=0
if total >=500 and total <=999:
    dicsount=price-(price*10  / 100)
elif total >=1000 and total<=1999:
    dicsount=price-(price*20 / 100)
elif total >=2000:
    dicsount=price-(price*30 / 100)
else:
    print("no dicsount")

extra_d=0

if item=='shirt':
    extra_d