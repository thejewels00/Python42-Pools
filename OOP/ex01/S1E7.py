from S1E9 import Character


class Baratheon(Character):
    """Class representing a Baratheon character, inheriting from Character."""

    def __init__(self, first_name, is_alive=True):
        """Constructor for Baratheon class."""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        """Method to change the health state of the Baratheon character."""
        self.is_alive = False

    def __str__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        return self.__str__()


class Lannister(Character):
    """Class representing a Lannister character, inheriting from Character."""

    def __init__(self, first_name, is_alive=True):
        """Constructor for Lannister class."""
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self):
        """Method to change the health state of the Lannister character."""
        self.is_alive = False

    def __str__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        return self.__str__()
    # c-a-d que cette fonction est une fonction de class est pas une 
    # foncton de l'instance

    @classmethod  
    def create_lannister(cls, first_name, is_alive=True):
        """Class method to create a Lannister character."""
        return cls(first_name, is_alive)
