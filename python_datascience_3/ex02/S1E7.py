from S1E9 import Character


class Baratheon(Character):
    """
    A class to represent a member of the Baratheon family.

    Attributes:
    -----------
    first_name : str
        The first name of the Baratheon family member.
    is_alive : bool
        A flag indicating whether the Baratheon family member is alive (default
        is True).
    family_name : str
        The family name, which is "Baratheon" for all instances of this class.
    eyes : str
        The eye color of the Baratheon family member, which is "brown" for all
        instances of this class.
    hairs : str
        The hair color of the Baratheon family member, which is "dark" for all
        instances of this class.
    """
    def __init__(self, first_name, is_alive=True):
        """
        Constructs all the necessary attributes for the Baratheon object.

        Parameters:
        -----------
        first_name : str
            The first name of the Baratheon family member.
        is_alive : bool, optional
            A flag indicating whether the Baratheon family member is alive
            (default is True).
        """
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        """
        Returns a string representation of the Baratheon object.

        Returns:
        --------
        str
            A string representation of the Baratheon object.
        """
        pass

    def __repr__(self):
        """
        Returns an unambiguous string representation of the Baratheon object.

        Returns:
        --------
        str
            An unambiguous string representation of the Baratheon object.
        """
        vector_str = f'{self.family_name}\', \'{self.eyes}\', \'{self.hairs}'
        return str(f'Vector: ({vector_str})')

    def die(self):
        """***METHOD***
    Sets the `is_alive` attribute to False if the character is currently alive.
        """
        if self.is_alive is True:
            self.is_alive = False


class Lannister(Character):
    """
    A class to represent a member of the Lannister family.

    Attributes:
    -----------
    first_name : str
        The first name of the Lannister family member.
    is_alive : bool
        A flag indicating whether the Lannister family member is alive (default
        is True).
    family_name : str
        The family name, which is "Lannister" for all instances of this class.
    eyes : str
        The eye color of the Lannister family member, which is "blue" for all
        instances of this class.
    hairs : str
        The hair color of the Lannister family member, which is "light" for all
        instances of this class.
    """
    def __init__(self, first_name, is_alive=True):
        """
        Constructs all the necessary attributes for the Lannister object.

        Parameters:
        -----------
        first_name : str
            The first name of the Lannister family member.
        is_alive : bool, optional
            A flag indicating whether the Lannister family member is alive
            (default is True).
        """
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self):
        """
        Returns a string representation of the Lannister object.

        Returns:
        --------
        str
            A string representation of the Lannister object.
        """
        pass

    def __repr__(self):
        """
        Returns an unambiguous string representation of the Lannister object.

        Returns:
        --------
        str
            An unambiguous string representation of the Lannister object.
        """
        vector_str = f'{self.family_name}\', \'{self.eyes}\', \'{self.hairs}'
        return str(f'Vector: ({vector_str})')

    def die(self):
        """***METHOD***
    Sets the `is_alive` attribute to False if the character is currently alive.
        """
        if self.is_alive is True:
            self.is_alive = False

    @classmethod
    def create_lannister(cls, first_name, is_alive):
        """
        Class method to create a Lannister object.

        Parameters:
        -----------
        first_name : str
            The first name of the Lannister family member.
        is_alive : bool, optional
            A flag indicating whether the Lannister family member is alive
            (default is True).

        Returns:
        --------
        Lannister
            A new instance of the Lannister class.
        """
        return cls(first_name, is_alive)
