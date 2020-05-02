'''
a = 10
def f1():
    a=777
    print(a) #777

def f2():
    print(a)  #10

f1()
f2()

'''

'''
a = 10
def f1():
    global a
    a = 777
    print(a)    #777

def f2():
    print(a)    #777

f1()
f2()
'''
'''
def f1():
    global a
    a = 10
    print(a)    #10

def f2():
    print(a)    #10

f1()
f2()
'''
'''
def f1():
    a = 10
    print(a)    #10

def f2():
    print(a)    #error

f1()
f2()
'''
a = 10


def f1():
    a = 777
    print(a)  # 777
    print(globals()['a'])  # 10


def f2():
    print(a)  # 10


f1()
f2()
