class Test:

    def __init__(self, x, y):
        self._x = 0

    def get_x(self):
        return self._x
    
    def set_x(self, value):
        self._x = value
    
    def print_x(self):
        print(self._x)

    def print_string(self, y):
        print(y)


object = Test(1,2)

object.print_string("Infra3")

