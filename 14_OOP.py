# Object-Oriented Programming

class Person:
    def getName(self):
        print("Mini")

    def getAge(self):
        print(24)


p = Person()
p.getName()
p.getAge()


# -----


class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        print("Your name is " + self.name)

    def getAge(self):
        print("Your age is " + self.age)


e = Employee("Mini", "25")

e.getName()
e.getAge()
