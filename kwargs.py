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

