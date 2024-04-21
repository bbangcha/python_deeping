def formatedNumber(n):
    return format(n, ',')

# 단리
def singleRateCarculator(m , t, r):

    totalMoney = 0
    totalRateMoney = 0

    for i in range(t):
        totalRateMoney += m * (r * 0.01)

    totalMoney = m + totalRateMoney
    return int(totalMoney)

# 월복리

def multiRateCalculator(m, t, r):

    t = t * 12
    rpm = (r / 12) * 0.01

    totalMoney = m

    for i in range(t):
        totalMoney += totalMoney * rpm

    return int(totalMoney)

money = int(input('예치금(원) : '))
term = int(input('기간(년) : '))
rate = int(input('연 이자율(%) : '))

print('[단리계산기]')
print('=' * 50)
print(f'예치금 : {formatedNumber(money)}원')
print(f'예치기간 : {term}년')
print(f'연 이율 : {rate}%')
print('-' * 50)
print(f'{term}년 후 총 수령액 : {formatedNumber(singleRateCarculator(money, term, rate))}')
print('=' * 50)


print('[월복리계산기]')
print('=' * 50)
print(f'예치금 : {formatedNumber(money)}원')
print(f'예치기간 : {term}년')
print(f'연 이율 : {rate}%')
print('-' * 50)
print(f'{term}년 후 총 수령액 : {formatedNumber(multiRateCalculator(money, term, rate))}')
print('=' * 50)

