from myapp.models.classa import ClassA


class ClassB:

    def __init__(self):
        self.a = None

    def get_a(self):
        self.a = ClassA()
        return self.a
