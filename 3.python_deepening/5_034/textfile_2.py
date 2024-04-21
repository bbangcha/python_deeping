import time

lt = time.localtime()
dataStr = ('[' + str(lt.tm_year) + '년' + str(lt.tm_mon) + '월'
           + str(lt.tm_mday) + '일]')

todaySchedule = input('오늘 일정 : ')

file = open('D:/pythonEx/pythontxt/test.txt', 'w')
file.write(dataStr + todaySchedule)
file.close()