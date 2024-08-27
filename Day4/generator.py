def test():
    yield "hello"
    yield "world"


out=test()
print(next(out))
print(next(out))
