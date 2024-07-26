from abc import ABC, abstractmethod


class Character(ABC):
    """
    Abstract base class representing a character in a game or story.

    This class serves as a blueprint for all character types, enforcing the
    implementation of the `die` method in subclasses. The `die` method should
    define the actions that take place when a character dies.

    Methods:
        die: Abstract method to be implemented by subclasses, defining the
        character's behavior upon death.
    """
    def __init__(self):
        """***CONSTRUCTOR***
        Initializes a new character.
        """
        pass

    @abstractmethod
    def die(self):
        """
    Abstract method to be implemented by subclasses.

    This method should contain the logic that occurs when the character dies.
        """
        pass


class Stark(Character):
    """***CLASS***
Represents a member of the Stark family, inheriting from the Character class.

This class models a character from the Stark family with a first name and a
status indicating whether they are alive or not. It implements the `die` method
from the Character base class.

Attributes:
    first_name (str): The first name of the Stark character.
    is_alive (bool): A boolean flag indicating whether the character is alive.
                        Defaults to True.

Methods:
    die: Sets the `is_alive` attribute to False if the character is currently
    alive.
    """
    def __init__(self, first_name, is_alive=True):
        """***CONSTRUCTOR***
        Initializes a new Stark character with a given first name and alive
        status.

        Args:
            first_name (str): The first name of the Stark character.
            is_alive (bool, optional): A boolean flag indicating whether the
            character is alive. Defaults to True.
        """
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """***METHOD***
    Sets the `is_alive` attribute to False if the character is currently alive.
        """
        if self.is_alive is True:
            self.is_alive = False
