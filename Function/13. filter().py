def isEven(x):
    if x % 2 == 0:
        return True
    else:
        return False


rangeno = int(input("Enter the 0 to range:"))
list1 = []

for x in range(0, rangeno):
    list1.append(x)

l1 = list(filter(isEven, list1))
print(l1)

# using lambda

l2 = list(filter(lambda x: x % 2 == 0, list1))
print(l2)
