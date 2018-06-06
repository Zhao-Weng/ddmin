from abc import ABC, abstractmethod
 
class AbstractClassExample(ABC):
 
    def __init__(self, value):
        self.value = value
        super().__init__()
    
    @abstractmethod
    def do_something(self):
        pass

class DoAdd42(AbstractClassExample):
    pass



# x = DoAdd42(4)   # type error 


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