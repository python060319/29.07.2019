
def dontChangeList(l1):
    # l1[0] = 12 -- Error!

list_ = [1,2,3]
dontChangeList(tuple(list_))
print(list_)
