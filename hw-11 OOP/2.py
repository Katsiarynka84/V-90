
class NumberField:

    def __set_name__(self, owner, name):
        self.name = name
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
    def __set__(self, instance, value):
        if type(value) in (int, float):
            instance.__dict__[self.name] = value
        else:
            raise ValueError('Некорректные данные')



class SimpleMathExpression:
    a = NumberField()
    b = NumberField()

    def __init__(self, a, b):
            self.a = a
            self.b = b

    def division(self):
        if self.b ==  0:
            raise ZeroDivisionError
        return round((self.a / self.b), 3)

    def multiplication(self):
        return self.a * self.b

    def addition(self):
        return self.a + self.b

    def subtraction(self):
        return self.a - self.b


obj = SimpleMathExpression(6.9, 0)
print(obj.division())
