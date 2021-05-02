import random


class Account:
    account_count = 0

    def __init__(self, name, money):
        self.deposit_count = 0
        self.deposit_log = []
        self.withdraw_log = []
        self.name = name
        self.money = money
        self.bank = "SC은행"

        num1 = str(random.randint(0, 999)).zfill(3)
        num2 = str(random.randint(0, 99)).zfill(2)
        num3 = str(random.randint(0, 999999)).zfill(6)
        self.account_number = num1 + '-' + num2 + '-' + num3  # 001-01-000001

        Account.account_count += 1

    @classmethod
    def get_account_num(cls):
        print(cls.account_count)

    def deposit(self, amount):
        if amount >= 1:
            self.money += amount
            self.deposit_log.append(amount)

            self.deposit_count += 1
            if not self.deposit_count % 5:
                self.money *= 1.01

    def deposit_history(self):
        for i in self.deposit_log:
            print(i)

    def withdraw(self, amount):
        if amount <= self.money:
            self.money -= amount
            self.withdraw_log.append(amount)

    def withdraw_history(self):
        for i in self.withdraw_log:
            print(i)

    def display_info(self):
        print(f"은행이름: {self.bank}")
        print(f"예금주: {self.name}")
        print(f"계좌번호: {self.account_number}")
        print(f"잔고: {self.money}")
