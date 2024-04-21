import ADictonary as dic

kte = dic.KorToEng()

kte.registWord('책', 'bok')
kte.registWord('나비', 'butterfly')
kte.registWord('연필', 'pencil')
kte.registWord('학생', 'student')
kte.registWord('선생님', 'teacher')

kte.printWord()

kte.updateWord('책', 'book')

kte.printWord()

print(f'책 : {kte.searchWord("책")}')
print(f'나비 : {kte.searchWord("나비")}')
print(f'선생님 : {kte.searchWord("선생님")}')

kte.removeWord('책')

kte.printWord()
