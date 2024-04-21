num1 = int(input('1보다 큰 정수 입력 : '))
num2 = int(input('1보다 큰 정수 입력 : '))
maxComNum = 0
for i in range(1, (num1 + 1)):
    if num1 % i == 0 and num2 % i == 0:
        maxComNum = i

try:
    with open('D:/pythonEx/pythontxt/5_065~069/maxComNum.txt', 'a') as f:
            f.write(f'{num1}과 {num2}의 최대공약수 : {maxComNum} \n')

except Exception as e:
    print(e)

else:
    print('max common factor write complete!')
