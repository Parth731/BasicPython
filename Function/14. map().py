def double(x):
    return 2 * x


l1 = [1, 2, 3, 4, 5]
l = list(map(double, l1))
print(l)

# using lambda

l = list(map(lambda x: 2 * x, l1))
print(l)

# To find square of given numbers

l = list(map(lambda x: x * x, l1))
print(l)

# multication of two list

l1 = [1, 2, 3, 4]
l2 = [2, 3, 4, 5]
l = list(map(lambda x, y: x * y, l1, l2))
print(l)
