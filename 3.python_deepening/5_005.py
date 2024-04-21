import random

def getOddRandomNumber():

    while True:
        rNum = random.randint(1, 100)
        if  rNum % 2 != 0:
            break

    return rNum

returnResult = getOddRandomNumber()
print(f'returnValue : {returnResult}')

print(f'returnValue : {getOddRandomNumber()}')
# return 값을 별도 (returnResult와 같은) 변수 지정 없이 함수명만을 print 해도 값을 출력할 수 있다