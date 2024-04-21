def add(n1, n2):
    print(n1 + n2)

def sub(n1, n2):
    print(n1 - n2)

def mul(n1, n2):
    print(n1 * n2)

def div(n1, n2):
    print(n1 / n2)

firstNumber = int(input('firstNumber : '))         #"10"
secondNumber = int(input('secondNumber : '))       #"0"

add(firstNumber, secondNumber)
sub(firstNumber, secondNumber)
mul(firstNumber, secondNumber)
div(firstNumber, secondNumber)        # "10"을 "0:으로 나눌서 없으므로 ZeroDivisionError 발생