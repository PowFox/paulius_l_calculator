class Calculator:
    def __init__(self, symbol: str, number: float) -> None:
        self.symbol = symbol
        self.number = number

    def add(self, new_number: int) -> float:
        return self.number + new_number

    def sub(self, new_number) -> float:
        return self.number + new_number

    def div(self, new_number) -> float:
        try:
            return self.number / new_number
        except Exception as err:
            print(f"Klaida: {err}")

    def mul(self) -> float:
        ...

    def calculate(self) -> float:
        ...
