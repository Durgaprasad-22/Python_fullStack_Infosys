class Sample:
    def __init__(self):
        print('it is a constructor')

    def show(self):
        print("show parent")
class Child(Sample):
    def show(self):
        super().show()
        print("from child")        

obj=Child()
obj.show()

