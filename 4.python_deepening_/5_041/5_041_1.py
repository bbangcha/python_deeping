# 거리 = 속도 * 시간

def getDistance(speed, hour, minute):
    distance = speed * (hour + (minute / 60))
    return distance

print('*' * 60)
s = float(input('속도(km/h) 입력 : '))
h = float(input('시간(h) 입력 : '))
m = float(input('시간(m) 입력 : '))
d = getDistance(s, h, m)
print(f'{s}km/h 속도로 {h}시간, {m}분 동안 이동한거리 : {d}km')
print('*' * 60)