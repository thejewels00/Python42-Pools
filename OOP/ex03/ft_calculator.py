class calculator:
    '''it's a calculator class who is abe to calculte some operation of vector with sclars'''
    def __init__(self, vector):
        '''constructor for calculator class'''
        self.vector = vector

    def __add__(self, object) -> None:
        ''' add a scalar to each element of the vector'''
        if isinstance(object, (int, float)):
            self.vector = ([x + object for x in self.vector])
        print(self.vector)

    def __mul__(self, object) -> None:
        ''' multiply a scalar to each element of the vector'''
        if isinstance(object, (int, float)):
            self.vector = ([x * object for x in self.vector])
        print(self.vector)
    def __sub__(self, object) -> None:
        ''' substract a scalar to each element of the vector'''
        if isinstance(object, (int, float)):
            self.vector = ([x - object for x in self.vector])
        print(self.vector)
    def __truediv__(self, object) -> None:
        ''' divide a scalar to each element of the vector'''
        if isinstance(object, (int, float)):
            if object == 0:
                print("Error: division by zero")
                return
            self.vector = ([x / object for x in self.vector])
        print(self.vector)
