'''
Lambda Function to find biggest of given values.

'''

s = lambda a, b: a if a > b else b
num1 = int(input("Enter the number1:"))
num2 = int(input("Enter the number2:"))
print(s(num1, num2))
