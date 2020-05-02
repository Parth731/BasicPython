def calc(num1, num2):
    sum = num1 + num2
    sub = num1 - num2
    mul = num1 * num2
    div = num1 / num2
    return sum, sub, mul, div


num1 = float(input("Enter num1:"))
num2 = float(input("Enter num2:"))

result = calc(num1, num2)

for x in result:
    print("result are:")
    print(x)
