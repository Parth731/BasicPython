def decor(func):
    def inner(name):
        if name == "sunny":
            print("hello", name, "bad morning")
        else:
            func(name)

    return inner


@decor
def wish(name):
    print("hello", name, "good morning")


wish("durga")
wish("ravi")
wish("sunny")
