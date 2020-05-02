def f1(n1, n2, n3=4, n4=8):
    print(n1, n2, n3, n4)
    print()


f1(3, 2)
f1(10, 20, 30, 40)
f1(25, 40, n4=100)
f1(n4=90, n1=80, n2=70)
# f1()    #invaild
# f(arg3=10,arg4=20,30,40)      ==>Invalid
# f(4,5,arg2=6)         ==>Invalid
#  f(4,5,arg3=5,arg5=6)     ==>Invalid
