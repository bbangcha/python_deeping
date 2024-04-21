uri = 'D:/pythonEx/pythontxt/'

scoreDic = {'kor' : 85, 'eng' : 90, 'mat' : 92, 'sic' : 79, 'his' : 82}

for key in scoreDic.keys():
    with open(uri + 'scoreDic.txt', 'a') as f:
        f.write(key + '\t:' + str(scoreDic[key]) + '\n')
