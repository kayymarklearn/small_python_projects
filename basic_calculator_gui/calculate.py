class Calculator:
    def __init__(self, *args):
        self.args = args
        self.result = 0

    def add(self):
        return sum(self.args)

    def sub(self):
        for digit in self.args:
            self.result -= int(digit)
        return self.result

    def multiply(self):
        for digit in self.args:
            self.result *= int(digit)
        return self.result
    def divide(self):
        for digit in self.args:
            self.result /= int(digit)
        return self.result