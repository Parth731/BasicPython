'''
 Write a function to find factorial of given number?
'''


def fact(num):
    result = 1
    while num >= 1:
        result = result * num
        num = num - 1
    return result


num = int(input("Enter the factorial range:"))
for x in range(1, num + 1):
    print("The Factorial of", x, "is :", fact(x))
