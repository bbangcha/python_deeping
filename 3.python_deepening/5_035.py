# import time
#
# lt = time.localtime()
#
# dateStr = '[' + time.strftime('%Y-%m-%d %I:%M:%S %p') + ']'
#
# # dateStr = ('[' + str(lt.tm_year) + '년' + str(lt.tm_mon) + '월'
# #            + str(lt.tm_mday) + '일]')
#
# todaySchedule = input('오늘 일정 : ')
#
# file = open('D:/pythonEx/pythontxt/test.txt', 'w')
# file.write(dateStr + todaySchedule)
# file.close()

file = open('D:/pythonEx/pythontxt/about python.txt', 'r')
str = file.read()
print(f'str : {str}')

file.close()

str = str.replace('Python','파이썬', 2)
print(f'str : {str}')

file = open('D:/pythonEx/pythontxt/about python.txt', 'w')
file.write(str)
file.close()