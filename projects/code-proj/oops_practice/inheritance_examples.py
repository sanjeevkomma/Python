class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"

class Student(Person):
    def __init__(self, name, age, college_name):
        super().__init__(name,age)
        self.college_name = college_name
    def __repr__(self):
        return repr((super().__repr__(),self.college_name))

person = Person('John', 20)
student = Student('John', 20, 'IIT')

print(person)
print(student)

# ---output--
# Person(name=John, age=20)
# ('Person(name=John, age=20)', 'IIT')
