def lockdown1(func):
    def inner():
        print("lockdown 1.0")
        func()

    return inner


def lockdown2(func):
    def inner():
        print("lockdown 2.0")
        func()

    return inner


def lockdown3(func):
    def inner():
        print("lockdown 3.0")
        func()

    return inner


@lockdown1
@lockdown2
@lockdown3
def wish():
    print("Stay Home, stay Safe, Stay healthy")


print(wish())
