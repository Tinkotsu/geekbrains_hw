class Car:
    def __init__(self, speed, color, name):
        self.speed = 0  # при создании машины устанавливаю скорость 0
        self.saved_speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        self.speed = self.saved_speed
        print(self.name + ' is going')

    def stop(self):
        self.speed = 0
        print(self.name + ' stopped')

    def turn(self, direction):
        if self.speed > 0:
            print(self.name + ' turned to the ' + direction)
        else:
            print(self.name + ' is not going. Can\'t turn to the ' + direction)

    def show_speed(self):
        print(self.name + '\'s speed is ' + str(self.speed))


class TownCar(Car):
    def show_speed(self):
        print(self.name + '\'s speed is ' + str(self.speed))
        if self.speed > 60:
            print('Too fast!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print(self.name + '\'s speed is ' + str(self.speed))
        if self.speed > 40:
            print('Too fast!')


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = True


tc = TownCar(100, 'red', 'golf')
tc.turn('right')
tc.show_speed()
print(tc.is_police)

pc = PoliceCar(150, 'black', 'lambo')
pc.go()
pc.show_speed()
print(pc.is_police)

sc = SportCar(200, 'red', 'ferrari')
sc.go()
sc.show_speed()
sc.turn('right')
sc.stop()

wrc = WorkCar(50, 'brown', 'polo')
wrc.go()
wrc.show_speed()
