from car_game import racing as rc
from car_game import car

myCarGame = rc.CarRacing()

car01 = car.Car('car01', 'white', 250)
car02 = car.Car('car02', 'black', 200)
car03 = car.Car('car03', 'yellow', 220)
car04 = car.Car('car04', 'red', 280)
car05 = car.Car('car05', 'blue', 150)

myCarGame.addCar(car01)
myCarGame.addCar(car02)
myCarGame.addCar(car03)
myCarGame.addCar(car04)
myCarGame.addCar(car05)

myCarGame.stertRacing()



