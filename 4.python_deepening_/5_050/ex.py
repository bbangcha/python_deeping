import combination as ct

numN = int(input('numN 입력 : '))
numR = int(input('numR 입력 : '))

ct.getCombinationCnt(numN, numR)
print(f'{numN}C{numR} : {ct.getCombinationCnt(numN, numR, logprint=False)
}')

listVar = [1, 2, 3, 4, 5, 6, 7, 8]
rVar = 3
ct.getCombinatios(listVar, rVar)
