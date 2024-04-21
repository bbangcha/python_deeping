inputNumber = int(input('0보다 큰 정수 입력 : '))

divisor = []
for number in range(1, (inputNumber + 1)):
    if inputNumber % number == 0:
        divisor.append(number)

if len(divisor) > 0:
    try:
        with open('D:/pythonEx/pythontxt/5_065~069/divisor.txt', 'a') as f:
            f.write(f'{inputNumber}의 약수 : ')
            f.write(f'{divisor}\n')
    except Exception as e:
        print(e)

    else:
        print('divisor write complete!')