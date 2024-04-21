def getCombinationCnt(n ,r, logprint = True):

    resultP = 1
    resultR = 1
    resultC = 1

    for n in range(n, (n-r), -1):
        resultP = resultP * n
    if logprint : print('resultP : {}'.format(resultP))

    for n in range(r, 0, -1):
        resultR = resultR * n
    if logprint : print('resultR : {}'.format(resultR))

    resultC = int(resultP / resultR)
    if logprint : print('resultC : {}'.format(resultC))

    return resultC

from itertools import combinations

def getCombinatios(ns, r):
    cList = list(combinations(ns, r))
    print(f'{len(ns)}C{r} : {len(cList)}')

    for n in combinations(ns, r):
        print(n, end='')