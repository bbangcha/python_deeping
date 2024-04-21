def exampleResult(s1, s2, s3, s4, s5):

    passAvgScore = 60; limitScore = 40

    def getTotal():
        totalScore = s1 + s2 + s3 + s4 + s5
        print(f'총점 : {totalScore}')
        return totalScore

    def getAervageg():
        avg = getTotal() / 5
        print(f'평균 : {avg}')
        return avg

    def printPassOrFail():
        print(f'{s1} : pass') if s1 >= limitScore else print(f'{s1} : fail')
        print(f'{s2} : pass') if s2 >= limitScore else print(f'{s2} : fail')
        print(f'{s3} : pass') if s3 >= limitScore else print(f'{s3} : fail')
        print(f'{s4} : pass') if s4 >= limitScore else print(f'{s4} : fail')
        print(f'{s5} : pass') if s5 >= limitScore else print(f'{s5} : fail')

    def printFinalPassOrFail():

        if getAervageg() >= passAvgScore:
            if (s1 >= limitScore and s2 >= limitScore and s3 >= limitScore and
                    s4 >= limitScore and s5 >= limitScore):
                print('Fimal Pass')
            else:
                print('Final Fail')
        else:
            print('Final Fail')

    getAervageg()
    printPassOrFail()
    printFinalPassOrFail()