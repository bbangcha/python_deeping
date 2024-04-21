scoreDic = {}

uri = 'D:/pythonEx/pythontxt/'

with open(uri +'scores.txt', 'r') as f:
    line = f.readline()

    while line != '':
        # print(line, end='')
        templist = line.split(':')
        scoreDic[templist[0]] = int(templist[1].strip('\n'))
        line = f.readline()

print(f'scoreDic : {scoreDic}')

