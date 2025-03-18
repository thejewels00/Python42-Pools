from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract base class for a character."""

    def __init__(self, first_name, is_alive=True):
        """Constructor for Character class."""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Method to change the health state of the character."""
        pass  # The pass statement is used as a placeholder for future code.


class Stark(Character):
    """Class representing a Stark character, inheriting from Character."""

    def __init__(self, first_name, is_alive=True):
        """Constructor for Stark class."""
        super().__init__(first_name, is_alive)

    def die(self):
        """Method to change the health state of the Stark character."""
        self.is_alive = False