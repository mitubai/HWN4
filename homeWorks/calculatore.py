class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def __add__(self, other):
        return self.num1 + other.num2

    def __sub__(self, other):
        return self.num1 - other.num2

    def __mul__(self, other):
        return self.num1 * other.num2

    def __truediv__(self, other):
        if other.num2 != 0:
            return self.num1 / other.num2
        else:
            return "Ошибка: деление на ноль"

# Пример использования
num1 = 10
num2 = 5
calc1 = Calculator(num1, num2)
calc2 = Calculator(20, 4)

print(f"{num1} + {num2} = {calc1 + calc2}")
print(f"{num1} - {num2} = {calc1 - calc2}")
print(f"{num1} * {num2} = {calc1 * calc2}")
print(f"{num1} / {num2} = {calc1 / calc2}")
