class Car:
    def __init__(self, car_type=None, year=None, color=None):
        if car_type:
            self._type = car_type
        if year:
            self._year = year
        if color:
            self._color = color

    @staticmethod
    def turn_on():
        print('Автомобиль заведён')

    @staticmethod
    def turn_off():
        print('Автомобиль заглушен')

    ##Поле color##
    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color

    car_color = property(get_color, set_color)



    def set_year(self, year):
        if isinstance(year,int) and 1900 < year < 2022:
            self._year = year
        else:
            print('Проверьте данные')

    def set_type(self, car_type):
        self._type = car_type


ferrari = Car()
bugatti = Car('sedan', 1955, 'green')
lamborghini = Car()

lamborghini.turn_on()
bugatti.set_type('cabriolet')
lamborghini.set_year(2023)
ferrari.car_color = 'blue'
print(ferrari.car_color)

print(ferrari.__dict__)
print(bugatti.__dict__)
print(lamborghini.__dict__)
