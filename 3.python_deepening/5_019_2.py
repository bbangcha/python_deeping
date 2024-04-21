class Calculator :

    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.result = 0

    def add(self):
        self.result = self.num1 + self.num2
        return self.result

    def sub(self):
        self.result = self.num1 - self.num2
        return self.result

    def mul(self):
        self.result = self.num1 * self.num2
        return self.result

    def div(self):
        self.result = self.num1 / self.num2
        return self.result


Calculator = Calculator()
Calculator.num1 = 10
Calculator.num2 = 20

print(f'Calculator.add : {Calculator.add()}')
print(f'Calculator.sub : {Calculator.sub()}')
print(f'Calculator.mul : {Calculator.mul()}')
print(f'Calculator.div : {Calculator.div()}')

Calculator.num1 = 30
Calculator.num2 = 40

print(f'Calculator.add : {Calculator.add()}')
print(f'Calculator.sub : {Calculator.sub()}')
print(f'Calculator.mul : {Calculator.mul()}')
print(f'Calculator.div : {Calculator.div()}')