def sequenceCal(n1, d, n):

    valueN = 0; sumN = 0;

    i = 1
    while i <= n:

        if i == 1:
            valueN = n1
            sumN += valueN
            print(f'{i}번째 항의 값 : {valueN}')
            print(f'{i}번째 항까지의 합 : {sumN}')

            i += 1
            continue

        valueN += d
        sumN += valueN
        print(f'{i}번째 항의 값 : {valueN}')
        print(f'{i}번째 항까지의 합 : {sumN}')

        i += 1


inputN1 = int(input('a1 입력 : '))
inputD1 = int(input('공차 입력 : '))
inputN = int(input('n 입력 : '))
sequenceCal(inputN1, inputD1, inputN)