'''
def foo(*args):
    print(args)
    print(type(args))
    print(args[0])
    #args[0] = 12 # Error!!

foo(1,2,3,'a', [1,2,3])

def mySum(*args):
    sum_of_args = sum(args)
    sum1 = 0
    for n in args:
        sum1 = sum1 + n
    l1 = [n for n in args]
    l2 = []
    for n in args:
        l2.append(n)
    l3 = list(args)
    set1 = set(args)

mySum(1, 2, 2, 3, 3)
# print sum of numbers
# return list of numbers -
#   given by *args
#   [1, 2, 2, 3, 3]
# modify *args to *myargs -
#   did it work?
# return the given args
#   without duplications

def foo(n, m, y = 1, *args):
    print(n)
    print(args)

foo(3)
'''

def kw(**kwargs):
    print(kwargs)
    print(type(kwargs))

kw(x = 1, y = 2, z = 3)

def printDictionary(k, **kwargs):
    if k in kwargs.keys():
        print('appears')
    else:
        print('not appear')
    print(kwargs.keys())
    print(kwargs.values())
    return list(kwargs.keys()) +\
        list(kwargs.values())

print(printDictionary('x', x=5, y=12))
# print if k appear in dictionary
# print dictionary values
# print dictionary keys
# return a list combined with keys
#   first and after that- values

