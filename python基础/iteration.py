def findMinAndMax(L):
    if len(L)==0:
        return (None,None)
    maxL=minL=L[0]
    for arg in L:
       if maxL<arg:
            maxL=arg
       if minL>arg:
            minL=arg
    return (minL,maxL)

if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
