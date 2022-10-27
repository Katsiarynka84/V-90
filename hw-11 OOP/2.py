class NumberField:
    def __set_name__(self, owner, name):
        self.name = f'_{name}'

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if type(value) in (int, float):
            instance.__dict__[self.name] = value
        else:
            raise ValueError('Некорректные данные')


class SimpleMathExpression:
    a = NumberField()
    b = NumberField()

    def __init__(self, a, b):
        self._a = a
        self._b = b

    def division(self):
        if self._b == 0:
            raise ZeroDivisionError
        return round((self._a / self._b), 3)

    def multiplication(self):
        return self._a * self._b

    def addition(self):
        return self._a + self._b

    def subtraction(self):
        return self._a - self._b


obj = SimpleMathExpression(6.9, 3)
print(obj.division())
print(obj.__dict__)
