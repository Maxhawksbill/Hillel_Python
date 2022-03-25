class Person:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def display_info(self):
        print(f'Name: {self.name}, Age: {self.age}, Sex: {self.sex}')


class Student(Person):
    def __init__(self, name, age, sex, university, grade):
        super().__init__(name, age, sex)
        self.university = university
        self.grade = grade

    def display_info(self):
        super().display_info()
        print(f'University: {self.university}, Grade: {self.grade}')


class Group(Student):
    def __init__(self, name, age, sex, university, grade, group_no):
        super().__init__(name, age, sex, university, grade)
        self.group_no = group_no

    def display_info(self):
        print(f'Student: {self.name} is in {self.group_no} group of the {self.university} University')


persons = [
    Person('Maria', 39, 'femail'),
    Student('Max', 20, 'man', 'Mechnikova', '3d Grade'),
    Group('Sergey', 25, 'man', 'Ushinskogo', '1st Grade', '123-OK')
            ]
for student in persons:
    student.display_info()
    print()
