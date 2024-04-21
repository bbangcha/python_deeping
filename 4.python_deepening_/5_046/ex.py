import passOrFail as pf

# 전역변수
if __name__ == '__main__':
    sub1 = int(input('과목 1 점수 입력 : '))
    sub2 = int(input('과목 2 점수 입력 : '))
    sub3 = int(input('과목 3 점수 입력 : '))
    sub4 = int(input('과목 4 점수 입력 : '))
    sub5 = int(input('과목 5 점수 입력 : '))

    pf.exampleResult(sub1, sub2, sub3, sub4, sub5)
