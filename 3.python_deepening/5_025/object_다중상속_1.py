class car01:
    def drive(self):
        print('drive() method called!!')

class car02:
    def turbo(self):
        print('turbo() method called!!')

class car03:
    def fly(self):
        print('fly() method called!!')

class car(car01, car02, car03):

    def __init__(self):
        pass

mycar = car()

mycar.drive()
mycar.turbo()
mycar.fly()
