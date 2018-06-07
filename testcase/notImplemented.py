

class MyBase():

    def f(self, x):
        raise NotImplementedError('Abstract method not implemented.')

class Child1(MyBase):
    def f(self, x):
        print(x)

class Child2(MyBase):
    pass

Child1().f(4)   # prints 4
Child2().f(4)   # raises implementation error
MyBase()  