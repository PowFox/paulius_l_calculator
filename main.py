class Calculator:
    def __init__(self, symbol: str, number: float) -> None:
        self.symbol = symbol
        self.number = number

    def add(self) -> float:
        return self.number + self.number

    def sub(self) -> float:
        return self.number - 15

    def div(self) -> float:
        return self.number / 2

    def mul(self) -> float:
        return self.number * self.number

    def calculate(self) -> float:
        if self.symbol == "+":
            return self.add()
        elif self.symbol == "-":
            return self.sub()
        elif self.symbol == "*":
            return self.mul()
        elif self.symbol == "/":
            return self.div()
        
        
calculator = Calculator("+", 12)

result = calculator.calculate()
print(result)