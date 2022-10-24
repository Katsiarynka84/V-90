def main():
    class Student:
        name = 'Ivan'
        group_number = '10A'
        age = 18

        def __init__(self, name='Ivan', group_number='10A', age=18):
            if isinstance(name, str) and name.isalpha():
                self.name = name
            else:
                raise ValueError('Некорректное имя')

            self.group_number = group_number

            if isinstance(age, int) and 15 < age < 60:
                self.age = age
            else:
                raise ValueError('Некорректный возраст')

        def get_name(self):
            return f'Имя студента: {self.name}'

        def get_age(self):
            return f'Возраст студента {self.name} - {self.age}'

        def get_group_number(self):
            return f'Группа студента {self.name}: {self.group_number}'

        def __str__(self):
            return f'Имя: {self.name}, группа: {self.group_number}, возраст: {self.age}'

        @classmethod
        def set_group_number(cls, group_number):
            Student.group_number = group_number

        @classmethod
        def set_name_age(cls, name, age):
            Student.name = name
            Student.age = age

    stud1 = Student('Maxim', '11b', 21)
    stud2 = Student('Tim', '7a', 25)
    stud3 = Student('Ivan', '11b', 32)
    stud4 = Student('Elena', '7a', 27)
    stud5 = Student('Ket', '7a', 28)

    print(stud1)
    print(stud2.get_name())
    print(stud3.get_age())
    Student.set_name_age('Mila', 33)
    print(stud5.get_group_number())

    print(Student.__dict__)


if __name__ == '__main__':
    main()
