class Car:
    def __init__(self, wheel, price):
        self.wheel = wheel
        self.price = price

    def info(self):
        print("바퀴수:", self.wheel)
        print("가격:", self.price)


class Elec_Car(Car):
    def __init__(self, wheel, price, drivetrain):
        super().__init__(wheel, price)
        self.drivetrain = drivetrain

    def info(self):
        super().info()
        print("구동계:", self.drivetrain)


class Auto_Car(Car):
    def __init__(self, wheel, price):
        super().__init__(wheel, price)


car = Elec_Car(2, 1000, "시마노")
car.info()
