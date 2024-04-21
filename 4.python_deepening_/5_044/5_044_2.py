# 등차 수열 공식 : an = a1 + (n-1)d
# 등차 수열 합 공식 : sn = n * (a1 +an) /2

def sequenceCal01(n1, d, n):

    # 등차 수열(일반항) 공식: an = a1 + (n-1) * d
    valueN = n1 + (n-1) * d
    print('{}번째 항의 값: {}'.format(n, valueN))

    # 등차 수열(합) 공식: sn = n(a1 + an) / 2
    sumN = n * (n1 + valueN) / 2
    print('{}번째 항까지의 합: {}'.format(n, int(sumN)))


inputN1 = int(input('a1 입력: '))
inputD = int(input('공차 입력: '))
inputN = int(input('n 입력: '))

sequenceCal01(inputN1, inputD, inputN)