from abc import ABCMeta
from abc import abstractmethod

class Airplane(metaclass=ABCMeta):

    @abstractmethod
    def flight(self):
        pass

    def forward(self):
        print('전진!!')

    def backward(self):
        print('후진!!')

class AirLiner(Airplane):

    def __init__(self, c):
        self.color = c

    def flight(self):
        print('시속 400km/h 비행!!')

class FighterPlane(Airplane):

    def __init__(self, c):
        self.color = c

    def flight(self):
        print('시속 800km/h 비행!!')

al = AirLiner('red')
al.flight()     # class Airplane을 상속 받았기 때문에 반드시 실행되어 하며 다른 클래스와 다른 기능으로 사용될 수 있다
al.forward()
al.backward()
print('-' * 25)
fl = FighterPlane('gray')
fl.flight()     # class Airplane을 상속 받았기 때문에 반드시 실행되어 하며 다른 클래스와 다른 기능으로 사용될 수 있다
fl.forward()
fl.backward()
