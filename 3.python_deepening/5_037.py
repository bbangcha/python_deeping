import random

uri = 'D:/pythonEx/pythontxt/'

def writeNimbers(nums):
    for idx, num in enumerate(nums):
        with open(uri + 'lotto.txt', 'a') as f:
            if idx < len(nums) - 2 :
                f.write(str(num) + ', ')
            elif idx == len(nums) - 2:
                f.write(str(num))
            elif idx == len(nums) - 1:
                f.write('\n')
                f.write('bonus' + str(num))
                f.write('\n')

rNums = random.sample(range(1, 46), 7)
print(f'rMums : {rNums}')

writeNimbers(rNums)
