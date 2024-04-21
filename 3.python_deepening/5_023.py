class P_Class:

    def __init__(self, pNum1, pNum2):
        print('[P_Class] __init__() called!!')

        self.pNum1 = pNum1
        self.pNum2 = pNum2


class C_Class(P_Class):

    def __init__(self, cNum1, cNum2):
        print('[C_Class] __init__() called!!')

        # P_Class.__init__(self, cNum1, cNum2) = "super"로 상위 class 속성을 사용할 수 있다!
        super().__init__(cNum1, cNum2)

        self.cNum1 = cNum1
        self.cNum2 = cNum2


cal = C_Class(10, 20)

