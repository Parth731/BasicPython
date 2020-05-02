def add(*n):
    total = 0
    for x in n:
        total = total + x
    print("The sum = ", total)


add()
add(10)
add(10, 20)
add(10, 20, 30, 40)


# diffent variable length

def f1(n1, *s):
    print(n1)
    for x in s:
        print(x)


f1(10)
f1(10, 20, 30, 40)
f1(10, 20, "A", "B")
f1(10, "A", 20, "B")


# diffent variable length

def f2(*s, n1):
    for x in s:
        print(x, end="")
    print(n1)


# f2("A","B",n1) #vaild
f2("A", "B", n1=10)
