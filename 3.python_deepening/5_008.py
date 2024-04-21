getTriangleArea = lambda n1 , n2 : n1 * n2 / 2
getSquareArea = lambda  n1 , n2 : n1 * n2
getCircleArea = lambda  r : r * r * 3.14

width = int(input('가로 입력 : '))
height = int(input('세로 입력 : '))
radius = int(input('반지름 입력 : '))

triangleValue = getTriangleArea(width, height)
SquareValue = getSquareArea(width, height)
circleValue = getCircleArea(radius)

print(f'삼각혁의 널이 : {triangleValue}')
print(f'사각혁의 널이 : {SquareValue}')
print(f'원의 널이 : {circleValue}')


