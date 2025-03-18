class calculator:
    '''it's a calculator class who is able to calculte some operation of vector with vectors'''
    def __init__(self, vector):
        '''constructor for calculator class'''
        self.vector = vector

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        '''dot product of two vectors'''
        print(f"Dot product: {sum([V1[i] * V2[i] for i in range(len(V1))])}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        '''add two vectors'''
        print(f"Add Vector is: {[V1[i] + V2[i] for i in range(len(V1))]}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        '''substract two vectors'''
        print(f"Sous Vector is: {[V1[i] - V2[i] for i in range(len(V1))]}")
