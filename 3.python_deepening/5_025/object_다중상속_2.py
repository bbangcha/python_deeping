class BasicCalculator:

    def add(self, n1, n2):
        return n1 + n2

    def sub(self, n1, n2):
        return n1 - n2

    def mul(self, n1, n2):
        return n1 * n2

    def div(self, n1, n2):
        return n1 / n2

class DevelopCalculator:

    def mod(self, n1, n2):
        return n1 % n2

    def flo(self, n1, n2):
        return n1 // n2

    def exp(self, n1, n2):
        return n1 ** n2

class NewCalculator(BasicCalculator, DevelopCalculator):
    def __init__(self):
        pass


cal = NewCalculator()

print(f'cal.add : {cal.add(10, 20)}')
print(f'cal.add : {cal.sub(10, 20)}')
print(f'cal.add : {cal.mul(10, 20)}')
print(f'cal.add : {cal.div(10, 20)}')
print(f'cal.mod : {cal.mod(10, 20)}')
print(f'cal.flo : {cal.flo(10, 20)}')
print(f'cal.exp : {cal.exp(2, 5)}')
