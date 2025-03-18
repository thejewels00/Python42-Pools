from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Class representing a King character, inheriting from Baratheon 
    and Lannister."""
    pass
    # def __init__(self, first_name, is_alive=True):
    #     """Constructor for King class."""
    #     super().__init__(first_name, is_alive)
    #     self.family_name = "Baratheon"
    #     self.eyes = "brown"

    def set_eyes(self, eyes):
        """Method to set the eyes of the King character."""
        self.eyes = eyes

    def set_hairs(self, hairs):
        """Method to set the hairs of the King character."""
        self.hairs = hairs

    def get_eyes(self):
        """Method to get the eyes of the King character."""
        return self.eyes

    def get_hairs(self):
        """Method to get the hairs of the King character."""
        return self.hairs
    