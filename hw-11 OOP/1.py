
class Student:
    _default_name = 'Ivan'
    _default_group_number = '10A'
    _default_age = 18

    @classmethod
    def set_default_group_number(cls, group_number):
        cls._default_group_number = group_number

    @classmethod
    def set_default_name_age(cls, name, age):
        cls._default_name = name
        cls._default_age = age

    def __init__(self, name=_default_name, group_number=_default_group_number, age=_default_age):
        self._name = name
        self._group_number = group_number
        self._age = age

    ##name##
    @property
    def stname(self):
        return f'Имя студента: {self._name}'

    @stname.setter
    def stname(self, name):
        if isinstance(name, str) and name.isalpha():
            self._name = name
        else:
            raise ValueError('Некорректное имя')

    @stname.deleter
    def stname(self):
        del self._name
    ### age ###
    def get_age(self):
        return f'Возраст студента {self._name} - {self._age}'

    def set_age(self, age):
        if isinstance(age, int) and 15 < age < 60:
            self._age = age
        else:
            raise ValueError('Некорректный возраст')

    def del_age(self):
        self._age = None

    st_age = property(get_age, set_age, del_age)

    def get_group_number(self):
        return f'Группа студента {self._name}: {self._group_number}'

    def __str__(self):
        return f'Имя: {self._name}, группа: {self._group_number}, возраст: {self._age}'


stud1 = Student('Maxim', '11b', 21)
stud2 = Student('Tim', '7a', 25)
stud3 = Student('Ivan', '11b', 32)
stud4 = Student('Elena', '7a', 27)
stud5 = Student('Ket', '7a', 28)

print(stud1)
print(stud2.stname)
print(stud3.st_age)
Student.set_default_name_age('Mila', 33)
print(stud5.get_group_number())

print(Student.__dict__)
stud1.stname = 'jack'
print(stud1.stname)
