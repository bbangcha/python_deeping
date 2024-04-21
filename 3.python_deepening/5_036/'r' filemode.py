uri = 'D:/pythonEx/pythontxt/'

file = open(uri + 'hello_01.txt', 'r')
str = file.read()
print(f'str : {str}')
file.close()