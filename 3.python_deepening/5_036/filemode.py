uri = 'D:/pythonEx/pythontxt/'

def writePrimeNumber(n):
    file = open(uri + 'prime_numbers.txt', 'a')
    file.write(str(n))
    file.write('\n')
    file.close()

inputNumber = int(input('0보다 큰 정수 입력 : '))
for number in range(2, (inputNumber + 1)):
    flag = True
    for n in range(2 , number):
        if number %n == 0:
            flag = False
            break

    if flag:
        writePrimeNumber(number)

