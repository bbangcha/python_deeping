everList = []; oddList = []; floatList = []

n = 1
while n < 6:

    try:
        num = float(input('input number : '))

    except:
        print('exception raise!!')
        print('input number again!!')
        continue

    else:
        if num - int(num) !=0:
            print('float number!')
            floatList.append(num)
        else:
            if num % 2 ==0:
                print('ever number!')
                everList.append(int(num))
            else:
                print('odd number!')
                oddList.append(int(num))

    n += 1

print(f'everList : {everList}')
print(f'oddList : {oddList}')
print(f'floatList : {floatList}')
