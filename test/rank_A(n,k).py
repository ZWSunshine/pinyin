#实现排列组合

import copy
lst = [1,2,3,4,5,6,7,8,9,10]
def permutation(lst,k):
    result = []
    length = len(lst)
    tmp = [0]*k
    def next_num(a,ni=0):

        if ni == k:
            result.append(copy.copy(tmp))
            return
        for lj in a:
            tmp[ni] = lj
            b = a[:]
            b.pop(a.index(lj))
            next_num(b,ni+1)
    c = lst[:]
    next_num(c,0)
    return result
print(permutation(lst,3))
print(len(permutation(lst,3)))