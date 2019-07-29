
def dontChangeList(l1):
    # l1[0] = 12 -- Error!

list_ = [1,2,3]
dontChangeList(tuple(list_))
print(list_)

# getUniqueTuple:
#  will get a list of numbers *args
#  return tuple from this list
#  contain only unique items
# getUniqueTuple(5, 5, 7, 9, 9, 8)
# *etgar return non-unique
#(7, 8)

def getUniqueTuple(*args):
    #return tuple([n for n in args\
    #      if args.count(n) == 1])
    res = []
    for n in args:
        if args.count(n) == 1:
            res.append(n)
    tup = tuple(res)
    return tup

def getNonUniqueTuple(*args):
    #return tuple([n for n in args\
    #      if args.count(n) == 1])
    res = []
    for n in args:
        if args.count(n) > 1:
            res.append(n)
    tup = tuple(res)
    return tup
