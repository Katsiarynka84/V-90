class Car:
    def __init__(self, car_type=None, year=None, color=None):
        if car_type:
            self.type = car_type
        if year:
            self.year = year
        if color:
            self.color = color

    @staticmethod
    def turn_on():
        print('Автомобиль заведён')

    @staticmethod
    def turn_off():
        print('Автомобиль заглушен')

    def set_color(self, color):
        self.color = color

    def set_year(self, year):
        if isinstance(year,int) and 1900 < year < 2022:
            self.year = year
        else:
            print('Проверьте данные')

    def set_type(self, car_type):
        self.type = car_type


ferrari = Car()
bugatti = Car('sedan', 1955, 'green')
lamborgini = Car()

lamborgini.turn_on()
bugatti.set_type('cabriolet')
lamborgini.set_year(2023)
ferrari.set_color('blue')

print(ferrari.__dict__)
print(bugatti.__dict__)
print(lamborgini.__dict__)
