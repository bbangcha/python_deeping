childPrice = 18000
infantPrice = 25000
adultPrice = 50000
specialDC = 50
def formatedNumber(n):
    return format(n, ',')
def printAirplaneReceiot(c1, c2, i1, i2, a1, a2):

    print('=' * 50)
    cp = c1 * childPrice
    cp_dc = int(c2 * childPrice * 0.5)
    print(f' 유아 : {c1}명 요금 \t: {formatedNumber(cp)}원,')
    print(f' 유아 할인 대상 : {c2}명 요금 \t: {formatedNumber(cp_dc)}원')

    ip = i1 * infantPrice
    ip_dc = int(i2 * infantPrice * 0.5)
    print(f' 소아 : {i1}명 요금 \t: {formatedNumber(ip)}원')
    print(f' 소아 할인 대상 \t: {i2}명 요금 : {formatedNumber(ip_dc)}원')

    ap = a1 * adultPrice
    ap_dc = int(a2 * adultPrice * 0.5)
    print(f' 성인 : {a1}명 요금 \t: {formatedNumber(ap)}원')
    print(f' 성인 할인 대상 : {a2}명 요금 \t: {formatedNumber(ap_dc)}원')
    print('=' * 50)
    print(f'Total : {formatedNumber(c1 + c2 + i1 + i2 + a1 + a2)}')
    print(f'TotalPrice : {formatedNumber(cp + cp_dc + ip + ip_dc + ap + ap_dc)}')
    print('=' * 50)

childCnt = int(input('유아 입력 : '))
specialChildCnt = int(input('할인 대상 유아 입력 : '))

infantCnt = int(input('소아 입력 : '))
specialInfantCnt = int(input('할인 대상 소아 입력 : '))

adultCnt = int(input('성인 입력 : '))
specialAdultCnt = int(input('할인 대상 성인 입력 : '))

printAirplaneReceiot(childCnt, specialChildCnt,
                     infantCnt, specialInfantCnt,
                     adultCnt, specialAdultCnt)





