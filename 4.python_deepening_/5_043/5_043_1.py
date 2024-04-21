def formatedNumber(n):
    return format(n, ',')

def recursionFun(n):

    if n == 1:
        return n

    return n * recursionFun(n-1)

inputNumber = int(input('input number : '))
print(formatedNumber(recursionFun(inputNumber)))
