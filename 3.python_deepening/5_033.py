class PsaawordLenthShortException(Exception):
    def __init__(self, str):
        super().__init__(f'{str}, : 길이 5미만')


class PsaawordLenthLongException(Exception):
    def __init__(self, str):
        super().__init__(f'{str}, : 길이 10초과')

class PsaawordWrongException(Exception):
    def __init__(self, str):
        super().__init__(f'{str}, : 잘못된 비밀번호')


adminPW = input('input admin password : ')

try:
    if len(adminPW) < 5:
        raise PsaawordLenthShortException(adminPW)
    elif len(adminPW) > 10:
        raise PsaawordLenthLongException(adminPW)
    elif adminPW != 'admin1234':
        raise PsaawordWrongException(adminPW)
    elif adminPW == 'admin1234':
        print('빙고!')

except PsaawordLenthShortException as e1:
    print(e1)

except PsaawordLenthLongException as e2:
    print(e2)

except PsaawordWrongException as e3:
    print(e3)
