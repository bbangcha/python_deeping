from arithmetic import basic_operation as bo
from arithmetic import developer_operation as do

from shape import circle_area as ca
from shape import triangle_square_area as tsa

inputNumber1 = float(input('숫자1 입력 : '))
inputNumber2 = float(input('숫자2 입력 : '))

print(f'{inputNumber1} + {inputNumber2} = {bo.add(inputNumber1, inputNumber2)}')
print(f'{inputNumber1} - {inputNumber2} = {bo.sub(inputNumber1, inputNumber2)}')
print(f'{inputNumber1} * {inputNumber2} = {bo.mul(inputNumber1, inputNumber2)}')
print(f'{inputNumber1} / {inputNumber2} = {bo.div(inputNumber1, inputNumber2)}')
print(f'{inputNumber1} % {inputNumber2} = {do.mod(inputNumber1, inputNumber2)}')
print(f'{inputNumber1} //  {inputNumber2} = {do.flo(inputNumber1, inputNumber2)}')
print(f'{inputNumber1} ** {inputNumber2} = {do.exp(inputNumber1, inputNumber2)}')

inputWidth = float(input('가로 길이 입력 : '))
inputHeight = float(input('세로 길이 입력 : '))
inputRadius = float(input('반지름 길이 입력 : '))

print(f'삼각형의 넓이 : {tsa.calTriangleArea(inputWidth, inputHeight)}')
print(f'사각형의 넓이 : {tsa.calSquareArea(inputWidth, inputHeight)}')
print(f'원의 넓이 : {ca.calCircleArea(inputRadius)}')
