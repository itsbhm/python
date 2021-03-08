class Parent:
    def __init__(self):
        print("This is the Parent class")

    def parentFunction(self):
        print("This is the Parent Function")


# p = Parent()
# p.parentFunction()


class Child(Parent):
    def __init__(self):
        print("This is the Child class")

    def childFunction(self):
        print("This is the Child Function")


c = Child()
c.childFunction()
c.parentFunction()


# Overriding

class P1:
    def __init__(self):
        pass

    def test(self):
        print("Parent")


class C1(P1):
    def __init__(self):
        pass

    def test(self):
        print("Child")


cp = C1()
cp.test()
