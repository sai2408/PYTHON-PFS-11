#Problem - 1
'''
def sample():
    s = 0
    for i in range(10):
        s = s + i
    yield s
x = sample()
print(x)
'''
#Problem - 2
'''
sample = ( num*num for i in range(5))
print(sample)
'''
#Problem - 3
'''
def sample123(n):
    for i in range(n):
        yield i
x = sample123(5)
print(x)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
'''
