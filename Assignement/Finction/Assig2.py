'''
 Write a function to check whether the given number is even or odd?

'''


def even_odd(num):
    if num % 2 == 0:
        print("Even number...")
    else:
        print("odd number...")


num = int(input("Enter the Number:"))
even_odd(num)
