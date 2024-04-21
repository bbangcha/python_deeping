import time

# 현지시간(  time.localtime()  )
lt = time.localtime()
print(f'time.localtime : {lt}')

print(f'lt.tm_year : {lt.tm_year}')
print(f'lt.tm_mon : {lt.tm_mon}')
print(f'lt.tm_mday : {lt.tm_mday}') # 며칠 = tm_mday
print(f'lt.tm_hour : {lt.tm_hour}')
print(f'lt.tm_min : {lt.tm_min}')
print(f'lt.tm_sec : {lt.tm_sec}')
print(f'lt.tm_wday : {lt.tm_wday}')  # 몇요일 = tm_wday
