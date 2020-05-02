'''
def outer():
    print("outer function started")
    def inner():
        print("inner function execution")
    print("outer function calling inner function")
    inner()
outer()
'''


# function can return other function

def outer():
    print("outer function started")

    def inner():
        print("inner function execution")

    print("outer function calling inner function")
    return inner


f1 = outer()
f1()
f1()
f1()
