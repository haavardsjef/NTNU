class Person:
    """Superclass"""

    def __init__(self):
        self.key = None

    def set_key(self, key):
        """Sets the key"""
        self.key = key

    def get_key(self):
        """Gets the key"""
        return self.key

    def operate_cipher(self):
        pass


class Sender:
    """Subklasse av Person"""

    def operate_cipher(self, key):
        caesar = Caeser(key)
        pass


class Reciever:
    """Subklasse av Person"""

    def operate_cipher(self):
        pass


class Hacker:
    """Subklasse av Person?"""
