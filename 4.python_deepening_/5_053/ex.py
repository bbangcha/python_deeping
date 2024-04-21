import member as mb

mems = mb.MemberRepository()

for i in range(3):
    mID = input('아이디 입력 : ')
    mPW = input('비밀번호 입력 : ')
    mem = mb.Member(mID, mPW)
    mems.addMember(mem)

mems.printMembers()

mems.loginMember('abc@gmail.com', '1234')
mems.loginMember('def@gmail.com', '5678')
mems.loginMember('ghi@gmail.com', '9012')

mems.remoneMember('abc@gmail.com', '1234')

mems.printMembers()

