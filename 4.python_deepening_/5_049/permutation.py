def getPermutationCnt(n, r, logPrint = True):

    result = 1
    for n in range(n, (n-r), -1):
        if logPrint : print('n:{}'.format(n))
        result = result * n

    return result

from itertools import permutations

def getPermutation(ns, r):

    pList = list(permutations(ns,r))
    print(f'{len(ns)}P{r} 개수 : {len(pList)}')

    for n in permutations(ns, r):
        print(n, end='')