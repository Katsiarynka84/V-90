class Math:

    def __init__(self, a, b):
        if type(a) in (int, float) and type(b) in (int, float):
            self.a = a
            self.b = b
        else:
            raise ValueError('Некорректные данные')

    def division(self):
        try:
            return round((self.a / self.b), 3)
        except ZeroDivisionError:
            return 'Ошибка деления на ноль'

    def multiplication(self):
        return self.a * self.b

    def addition(self):
        return self.a + self.b

    def subtraction(self):
        return self.a - self.b


obj = Math(6.9, 17)
print(obj.division())
