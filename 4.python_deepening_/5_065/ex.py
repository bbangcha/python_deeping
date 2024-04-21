import diary

members = {} # id와 pw로 관리해야 하기 때문에 dicionary로 설정
uri = 'D:/pythonEx/pythontxt/5_065~069'

def printMembers():
    for m in members.keys():
        print(f'ID : {m}, \t PW : {members[m]}')

while True:
    selectNum = int(input('1. 회원가입, 2. 한줄일기쓰기, 3. 일기보기, 4.종료'))

    if selectNum == 1:
        mId = input('input ID : ')
        mPw = input('input PW : ')
        members[mId] = mPw
        printMembers()

    elif selectNum == 2:
        mId = input('input ID : ')
        mPw = input('input PW : ')

        if mId in members and members[mId] == mPw:
            print('login success!')
            fileName = 'myDairy_ ' + mId + '.txt'
            data = input('오늘 하루 인상 싶은 일을 기록하세요.')
            diary.writeDiary(uri, fileName, data)

        else:
            print('login fail!')
            printMembers()

    elif selectNum == 3:
        mId = input('input ID : ')
        mPw = input('input PW : ')

        if mId in members and members[mId] == mPw:
            print('login success!')
            fileName = 'myDairy_ ' + mId + '.txt'
            datas = diary.readDiart(uri, fileName)
            for d in datas:
                print(d, end='')

        else:
            print('login fail!')
            printMembers()

    elif selectNum == 4:
        print('bye~')
        break