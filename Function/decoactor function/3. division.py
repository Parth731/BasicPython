def samrt_division(function):
    def inner(a, b):
        print("we are division", a, "with", b)
        if b == 0:
            print("0 is divide")
            return
        else:
            return function(a, b)

    return inner


@samrt_division
def division(a, b):
    return a / b


print(division(20, 10))
print(division(20, 0))
