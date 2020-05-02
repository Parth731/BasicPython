def decor(func):
    def inner(name):
        if name == "sunny":
            print("hello", name, "bad morning")
        else:
            func(name)

    return inner


def wish(name):
    print("hello", name, "good morning")


decorfunction = decor(wish)

wish("durga")
wish("parth")
decorfunction("durga")
decorfunction("parth")
