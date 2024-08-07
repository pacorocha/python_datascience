from S1E7 import Baratheon, Lannister

class King(Baratheon, Lannister):
    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)
    @property
    def eyes(self):
        '''The eyes property.'''
        return self._eyes

    @eyes.setter
    def eyes(self, value):
        self._eyes = value

    def set_eyes(self, value):
        self._eyes = value

    def get_eyes(self):
        return self.eyes

    @property
    def hairs(self):
        '''The hairs property.'''
        return self._hairs

    @hairs.setter
    def hairs(self, value):
        self._hairs = value

    def set_hairs(self, value):
        self.hairs = value

    def get_hairs(self):
        return self.hairs
