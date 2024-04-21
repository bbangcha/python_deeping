def fun1():
    print('fun1 호출!!')
    fun2()
    print('fun2가 최종적으로(실행될 fun3 함수까지) 실행된 이후에 다시 fun1로 돌아가서 실행 후 호출!!')
def fun2():
    print('fun2 호출!!')
    fun3()

def fun3():
    print('fun3 호출!!')

fun1()
