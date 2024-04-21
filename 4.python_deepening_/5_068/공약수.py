num1 = int(input('1보다 큰 정수 입력 : '))
num2 = int(input('1보다 큰 정수 입력 : '))

common = []
for i in range(1, (num1 + 1)):
    if num1 % i == 0 and num2 % i == 0:
        common.append(i)

if len(common) > 0:
    try:
        with open('D:/pythonEx/pythontxt/5_065~069/common.txt', 'a') as f:
            f.write(f'{num1}과 {num2}의 공약수 : ')
            f.write(f'{common} \n')

    except Exception as e:
        print(e)

    else:
        print('common factor write complete!')
