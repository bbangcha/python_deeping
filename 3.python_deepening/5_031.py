everList = []; oddList = []; floatList = []
dataList = []

n = 1
while n < 6:

    try:
        data = input('input numer : ')
        flaotnum = float(data)

    except:
        print('exception raise!!')
        print('input number again!!')
        continue

    else:
        if flaotnum - int(flaotnum) !=0:
            print('float number!')
            floatList.append(flaotnum)
        else:
            if flaotnum % 2 == 0:
                print('ever number!')
                everList.append(int(flaotnum))
            else:
                print('odd number!')
                oddList.append(int(flaotnum))

        n += 1

    finally:
        dataList.append(data)


print(f'everList : {everList}')
print(f'oddList : {oddList}')
print(f'floatList : {floatList}')
print(f'dataList : {dataList}')