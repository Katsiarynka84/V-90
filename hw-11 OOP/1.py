def main():
    class Student:
        _default_name = 'Ivan'
        _default_group_number = '10A'
        _default_age = 18

        def __init__(self, name='Ivan', group_number='10A', age=18):
            if isinstance(name, str) and name.isalpha():
                self._name = name
            else:
                raise ValueError('Некорректное имя')

            self._group_number = group_number

            if isinstance(age, int) and 15 < age < 60:
                self._age = age
            else:
                raise ValueError('Некорректный возраст')

        @property
        def stname(self):
            return f'Имя студента: {self._name}'

        @stname.setter
        def stname(self, name):
            self._name = name

        @stname.deleter
        def stname(self):
            del self._name

        # stname = property(get_name, set_name)
        # stname = stname.setter(set_name)
        # stname = stname.getter(get_name)

        #
        # def get_age(self):
        #     return f'Возраст студента {self.name} - {self._default_age}'
        #
        # def get_group_number(self):
        #     return f'Группа студента {self.name}: {self.group_number}'

        # def __str__(self):
        #     return f'Имя: {self.name}, группа: {self.group_number}, возраст: {self._default_age}'

        @classmethod
        def set_group_number(cls, group_number):
            cls._default_group_number = group_number

        @classmethod
        def set_name_age(cls, name, age):
            cls._default_name = name
            cls._default_age = age

    stud1 = Student('Maxim', '11b', 21)
    stud2 = Student('Tim', '7a', 25)
    stud3 = Student('Ivan', '11b', 32)
    stud4 = Student('Elena', '7a', 27)
    stud5 = Student('Ket', '7a', 28)

    # print(stud1)
    # print(stud2.get_name())
    # print(stud3.get_age())
    # Student.set_name_age('Mila', 33)
    # print(stud5.get_group_number())
    #
    # print(Student.__dict__)
    stud1.stname = 'jack'
    print(stud1.stname)


if __name__ == '__main__':
    main()
