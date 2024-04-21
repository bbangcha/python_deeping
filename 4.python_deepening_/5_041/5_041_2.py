# 시간

def getTime(speed, distance):
    time = distance / speed
    print(f'time : {time}')
    h = int(time)
    m = int((time - h) * 100 * 60 / 100)

    return [h ,m] #시간 "time"을 리스트화 해주기 ( 첫번째 값[h]는 [0], 두번째값[m]은 [1] )

# 100 : 75 = 60 : X --> X = 75 * 60 / 100

print('*' * 60)
s = float(input('속도(km/h) 입력 : '))
d = float(input('거리(km) 입력 : '))
t = getTime(s, d)
print(f'{s}km/h {d}(km) 이동한 시간 : {t[0]}시간 {t[1]}분')

print('*' * 60)