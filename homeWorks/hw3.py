import random

class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        if random.random() < .30:  # 30% шанс на джекпот
            self.__Jackpot()
            print("Джекпот! Баланс увеличен в 10 раз!")
        print(f"Пополнено: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Снято: {self.balance}")
        else:
            print("Ошибка, лол что за троллинг.")

    def _kill(self):
        self.balance = 0
        print("Ты Просрал свой баланс поздравляю.")

    def display_balance(self):
        print(f"Баланс: {self.balance}")

    def __Jackpot(self):
        self.balance *= 10

    def _connect_with_other(self, other):
        if isinstance(other, Bank):
            self.balance += other.balance
        else:
            print("Переданный объект не является экземпляром Bank.")

    def __str__(self):
        return f"Имя: {self.name}, Баланс: {self.balance}"

# Создание экземпляров для демонстрации
Idiot = Bank("Idiot", 0)
Smart = Bank("Smart", 100)

while True:
    Info = input(f"Введите 'пополнить', для пополнения, 'обнулить', для обнуления, 'объединить', для объединения балансов, 'выход' для выхода:")

    if Info == "пополнить":
        try:
            deposit_amount = float(input("Введите сумму для пополнения: "))
            Idiot.deposit(deposit_amount)
        except ValueError:
            print("Пожалуйста, введите корректную сумму.")
    elif Info == "обнулить":
        Idiot._kill()
    elif Info == "объединить":
        Idiot._merge_balance_with(Smart)
        print(f"Баланс Idiot после объединения: {Idiot.balance}")
        print(f"Баланс Smart остается неизменным: {Smart.balance}")
    elif Info == "выход":
        print("Завершение работы.")
        break
    else:
        print("Лол да ты гений.")

    print(Idiot)
