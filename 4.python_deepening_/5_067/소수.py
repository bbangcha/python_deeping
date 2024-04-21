inputNumber = int(input('0보다 큰 정수 입력 : '))

prime = []
for number in range(2, (inputNumber + 1)):
    flag = True
    for n in range(2, number):
        if number % n ==0:
            flag = False
            break

    if flag:
        prime.append(number)

if len(prime) > 0:
    try:
        with open('D:/pythonEx/pythontxt/5_065~069/prime.txt', 'a') as f:
            f.write(f'{inputNumber}까지의 소수 : ')
            f.write(f'{prime}\n')
    except Exception as e:
        print(e)

    else:
        print('prime write complete!')