from functools import *

no = int(input("Enter the range:"))
l1 = []

for x in range(10, no, 10):
    l1.append(x)

print(l1)
l = reduce(lambda x, y: x + y, l1)
print(l)
l = reduce(lambda x, y: x * y, l1)
print(l)
