ship1 = 3
ship2 = 4
ship3 = 5

maxDay = 0 # 최대공약수

for i in range(1, ship1 + 1):
    if ship1 % i == 0 and ship2 % i == 0:
        maxDay = i

minDay =(ship1 * ship2) // maxDay # 최소공배수

newDay = minDay

for i in range(1, (newDay + 1)):
    if newDay % i ==0 and ship3 % i == 0:
        maxDay = i

minDay = (newDay * ship3) // maxDay

print(f'minDay : {minDay}')
print(f'maxDay : {maxDay}')


from datetime import datetime
from datetime import timedelta

n = 1
baseTime = datetime(2023, 1, 1, 10, 0, 0)

with open('D:/pythonEx/pythontxt/5_065~069/arrive.txt', 'a') as f:
    f.write(f'2023년 모든 선박 입항일\n')
    f.write(f'{baseTime}\n')

nextTime = baseTime + timedelta(days=minDay)
while True:

    with open('D:/pythonEx/pythontxt/5_065~069/arrive.txt', 'a') as f:
        f.write(f'{nextTime}\n')

    nextTime = nextTime + timedelta(days=minDay)
    if nextTime.year > 2023:
        break