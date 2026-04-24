a=[1,2,65,500]
print(a)

a[3]=43

print(a)
print(a[3])

print('-----------------------------------------------------------------------------------------------------')

b=[1.3,'hii',50,54.5]

print(b)
print(b[1])

print('-----------------------------------------------------------------------------------------------------')

# we use [-1] to access last element

c=[1,2,3,4,5]

print(c[-1])
print(c[-2])

a.reverse()
a.sort() # sort into assending 
c.clear() #clear list

a.append(100) # add new value
a.insert(2,999) # add new value at specific index number
print(a)

print('-----------------------------------------------------------------------------------------------------')

m=[1,2,5,40,5]

m.reverse()


print(m)
m.sort()
print(m)

print(len(m))

# Copy list example
a = [10, 20, 30]

b = a.copy() 
b.append(70)


c = [30, 40]
d = c   

d.append(70)



a1 = [1, 2, 3]

a1.remove(2)   # removes value 2


a2= [1, 2, 3]
a2.pop(2)      # removes element at index 2

# Remove duplicate example
v = [1, 2, 2, 3]

v.remove(2)   # removes first occurrence of 2

# Append vs Extend
a1 = [1, 2, 3]
a2 = [3, 4]

a1.append(a2)
  # [1, 2, 3, [3, 4]]


# extend → adds elements individually
a1 = [1, 2, 3]
a2 = [3, 4]

a1.extend(a2)
# [1, 2, 3, 3, 4]

print('-----------------------------------------------------------------------------------------------------')

x=[10,20,30,40,50,60] #count

#list object - method 

y=x.count(10)

print(x)
print(y)

x1=['ds','da','py','ds']

x2=x1.count('ds')

print(x1)
print(x2)

print('-----------------------------------------------------------------------------------------------------')

k=[10,20,30,40]
n=k.copy()
k.append(50)

print(k)
print(n)

k1=[10,20,30,40,50]

n1=k1

k1.append(540)

print(k1)
print(n1)

print('-----------------------------------------------------------------------------------------------------')

r=[10,20,30,40,50]
print(r.index(30))

r1=[10,20,30,40,50,10]
print(r.index(10))

r2=[10,20,30,40,50]
print(r.index(60))

print=('-----------------------------------------------------------------------------------------------------')

