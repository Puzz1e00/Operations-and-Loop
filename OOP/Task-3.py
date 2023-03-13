class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        print(f'Name = {self.name}\n'f'Age = {self.age}')


class Employee(Person):
    def __init__(self, name, age, salary, designation):
        self.salary = salary
        self.designation = designation
        super().__init__(name, age)

    def get_details(self):
        super().get_details()
        print(f'Salary = {self.salary}\nDesignation = {self.designation} ')


# person1 = Person('Ram', 22 )
employee1 = Employee('ram', 22, 200000, 'Manager')
# print(person1.get_details())
print(employee1.get_details())