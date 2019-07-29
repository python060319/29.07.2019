
def foo(*args):
    print(args)
    print(type(args))
    print(args[0])
    #args[0] = 12 # Error!!

foo(1,2,3,'a', [1,2,3])

mySum(1, 2, 2, 3, 3)
# print sum of numbers
# return list of numbers -
#   given by *args
#   [1, 2, 2, 3, 3]
# modify *args to *myargs -
#   did it work?
# return the given args
#   without duplications
foo( )


