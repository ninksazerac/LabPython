class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def sub(self):
        return self.num1 - self.num2

    def mul(self):
        return self.num1 * self.num2

    def div(self):
        if self.num2 != 0:
            return self.num1 / self.num2


x, y = input('Enter num1 num2 : ').split(',')
answer = Calculator(int(x), int(y))

print(answer.add(), answer.sub(), answer.mul(), answer.div(), sep='\n')
