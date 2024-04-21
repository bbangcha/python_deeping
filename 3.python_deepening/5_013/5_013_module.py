import unitConversion as uc

if __name__ == '__main__':
    inputNumber = int(input('길이(cm) : '))

    returnValue = uc.cmToMm(inputNumber)
    print(f'returnValue : {returnValue}mm')

    returnValue = uc.cmToInch(inputNumber)
    print(f'returnValue : {returnValue}inch')

    returnValue = uc.cmToM(inputNumber)
    print(f'returnValue : {returnValue}M')

    returnValue = uc.cmToFt(inputNumber)
    print(f'returnValue : {returnValue}Ft')