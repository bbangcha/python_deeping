nums = []

n = 1
while n < 6:

    try:
        num = int(input('input number : '))
    except:
        print('예외발생!')
        continue

    nums.append(num)
    n += 1

print(f'nums : {nums}')