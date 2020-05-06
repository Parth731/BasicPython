def mygen():
    yield 'a'
    yield 'b'
    yield 'a'


g = mygen()
print(type(g))

print(next(g))
print(next(g))
print(next(g))
