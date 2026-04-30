# 1) Create an empty list and use append() to add 5 names
name = []
name.append("Rahul")
name.append("Aman")
name.append("Priya")
name.append("Neha")
name.append("Karan")
print(name)

print('-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*')

# 2) Insert 100 at index 2
numbers = [10, 20, 30, 40]
numbers.insert(2, 100)
print(numbers)

print('-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*')

# 3) Remove "apple"
fruit = ["apple", "banana", "mango"]
fruit.remove("apple")
print(fruit)

print('-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*')

# 4) Pop last item
list1 = [1, 2, 3, 4]
list1.pop()
print(list1)

print('-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*')

# 5) Pop item at index 1
list2 = [10, 20, 30, 40]
list2.pop(1)
print(list2)

print('-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*')

# 6) Extend list
a = [1, 2, 3]
a.extend([4, 5, 6])
print(a)

print('-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*')

# 7) Reverse list
letters = ["a", "b", "c"]
letters.reverse()
print(letters)

print('-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*')

# 8) Sort ascending
nums1 = [5, 2, 9, 1]
nums1.sort()
print(nums1)

print('-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*')

# 9) Sort descending
nums2 = [5, 2, 9, 1]
nums2.sort(reverse=True)
print(nums2)

print('-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*')

# 10) Count "python"
sub= ["python", "java", "python", "c++"]
sub2=sub.count("python")
print(sub2)

print('-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*')

# 11) Find index of banana (incomplete)
fruits2=["apple", "banana", "mango"]
position=fruits2.index("banana")
print(position)
print('-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*')

# 12) Copy list
a=[10, 20, 30]
b=a.copy()

print(a)
print(b)

print('-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*')

# 13) Clear list
temp=[1, 2, 3]
temp.clear()
print(temp)

print('-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*')

# 14) Append 6
b1= [1, 2, 3, 4, 5]
b1.append(6)
print(b1)

print('-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*')

# 15) Extend colors
color=["red", "blue"]
color.extend(["green", "yellow"])
print(color)

print('-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*')

# 16) Insert 5 at beginning
c = [7, 8, 9]
c.insert(0, 5)
print(c)

print('-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*')

# 17) Remove 33
d = [11, 22, 33, 44]
d.remove(33)
print(d)

print('-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*')

# 18) Count 6
e = [3, 6, 9, 12, 6]
print(e.count(6))

print('-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*')

# 19) Reverse of list
rev= ["x", "y", "z"]
rev.reverse()
print(rev)

print('-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*')

# 20) Sort numbers ascending
f = [100, 50, 200, 150]
f.sort()
print(f)
