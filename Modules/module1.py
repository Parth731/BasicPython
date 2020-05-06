# print("This is from module1")


def f1():
    if __name__ == "__main__":
        print("The code executed as program")
    else:
        print("The code excuted as module from same other program")


f1()
