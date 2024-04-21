def printArea():
    triangleArea = width * height / 2
    squareArea = width * height

    print('삼각형의 넓이 : {}'.format(triangleArea))
    print('사각형의 넓이 : {}'.format(squareArea))

width = int(input('가로 길이 : '))
height = int(input('가로 길이 : '))

printArea()