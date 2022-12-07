class Student:
    def __init__(self, id, name, language = "python"):
        self.id = id
        self.name = name
        self.language = language

    def __str__(self):
        return f'[{self.id}] {self.name} studies {self.language}'


print(Student(1, 'Bob', "Python"))  # should print: [1] Bob studies Python
print(Student(2, 'Mark', "Java"))  # should print: [2] Mark studies Java
print(Student(3, 'Kate'))  # should print: [3] Kate studies Python