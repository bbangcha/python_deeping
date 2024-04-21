class Car:

    def __init__(self, color, length):
        self.color = color
        self.length = length

    def doStop(self):
        print('STOP!!')

    def doStart(self):
        print('START!!')

    def printCarInfo(self):
        print(f'self.color : {self.color}')
        print(f'self.length : {self.length}')



car1 = Car('red', 200)
car2 = Car('blue', 300)

car1.printCarInfo()
car2.printCarInfo()

car1.doStop()
car1.doStart()