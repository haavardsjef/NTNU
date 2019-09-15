import Cypher

class Person:
    """Superclass"""

    def __init__(self):
        self.key = None
        self.cipher = None
        self.encoded_text = None

    def set_key(self, key):
        """Sets the key"""
        self.key = key

    def get_key(self):
        """Gets the key"""
        return self.key

    def set_cipher(self, cipher):
        self.cipher = cipher

    def get_cipher(self):
        return self.cipher

    def set_encoded_text(self, decoded_text):
        self.encoded_text = decoded_text

    def get_encoded_text(self):
        return self.encoded_text

    def operate_cipher(self):
        pass


class Sender(Person):
    """Subklasse av Person"""
    def __init__(self):
        Person.__init__(self)

    def operate_cipher(self):
        text = input("Text to encrypt: ")
        cipher = self.get_cipher()
        self.set_key(cipher.generate_keys())
        self.encoded_text = cipher.encode(text, self.get_key())


class Reciever(Person):
    """Subklasse av Person"""
    def __init__(self):
        Person.__init__(self)
        self.encoded_text = None



    def operate_cipher(self):
        cipher = self.get_cipher()
        print("Dekryptert melding: ", cipher.decode(self.get_encoded_text(), self.get_key()))


class Hacker:
    """Subklasse av Person?"""





def pick_cipher():
    print("Type cipher?" + "\n" + "0 = Caesar" + "\n" + \
     "1 = Multiplikativ" + "\n" + "2 = Affine" + "\n" + "3 = Unbreakable" + "\n" + "4 = RSA")
    type_cipher = int(input())
    if type_cipher == 0:
        cipher_1 = Cypher.Caesar()
        cipher_2 = Cypher.Caesar()
    elif type_cipher == 1:
        cipher_1 = Cypher.Multiplicative()
        cipher_2 = Cypher.Multiplicative()
    elif type_cipher == 2:
        cipher_1 = Cypher.Affine()
        cipher_2 = Cypher.Affine()
    elif type_cipher == 3:
        cipher_1 = Cypher.Unbreakable()
        cipher_2 = Cypher.Unbreakable()
    elif type_cipher == 4:
        cipher_1 = Cypher.RSA()
        cipher_2 = Cypher.RSA()
    return cipher_1, cipher_2


SENDER = Sender()
RECIEVER = Reciever()
CIPHER1, CIPHER2 = pick_cipher()
SENDER.set_cipher(CIPHER1)
RECIEVER.set_cipher(CIPHER2)
SENDER.operate_cipher()
RECIEVER.set_encoded_text(SENDER.get_encoded_text())
RECIEVER.set_key(SENDER.get_key())
RECIEVER.operate_cipher()
input()
