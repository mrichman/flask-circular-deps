from myapp.models.classb import ClassB


class ClassA:

    def __init__(self):
        self.b = None

    def get_b(self):
        self.b = ClassB()
        return self.b
