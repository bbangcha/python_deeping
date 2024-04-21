def prinScore(korScore, engScore, matScore):
    sum = korScore + engScore + matScore
    avg = sum / 3

    print(f'총점 : {sum}')
    print(f'평균 : {round(avg, 2)}')

korScore = int(input('국어 점수 입력 : '))
engScore = int(input('영어 점수 입력 : '))
matScore = int(input('수학 점수 입력 : '))

prinScore(korScore, engScore, matScore)
