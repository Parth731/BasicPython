def countreverse(num):
    while num >= 0:
        yield num
        num = num - 1


num = int(input("Enter the number:"))
value = countreverse(num)

for x in value:
    print(x, end=" ")
