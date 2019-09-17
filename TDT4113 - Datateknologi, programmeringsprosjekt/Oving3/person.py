import Cypher
import crypto_utils

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
        if not isinstance(cipher, Cypher.RSA):
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


class Hacker(Person):
    """Subklasse av Person?"""

    def __init__(self):
        Person.__init__(self)
        self.words = []
        self.import_words()

    def hack(self, encoded_text, cipher):
        if isinstance(cipher, Cypher.Caesar) or isinstance(cipher, Cypher.Multiplicative):
            key = 0
            index = -1
            while index == -1:
                decoded_text = cipher.decode(encoded_text, key)
                index = self.validate_word(decoded_text)
                key += 1
            print(key-1)
            print("Hackers most probable word: ", self.words[index])
        if isinstance(cipher, Cypher.Affine):
            key_1 = 0
            key_2 = 0
            index = -1

            while index == -1:
                while index == -1 and key_1 < 100:
                    if crypto_utils.modular_inverse(key_1, cipher.alphabet_size):
                        decoded_text = cipher.decode(encoded_text, (key_1, key_2))
                        index = self.validate_word(decoded_text)
                    key_1 += 1
                    print("i: ", key_1, " j:  ", key_2)
                key_1 = 0
                key_2 += 1
            print("Hackers most probable word: ", self.words[index])
        if isinstance(cipher, Cypher.Unbreakable):
            key = 0
            index = -1
            while index == -1:
                decoded_text = cipher.decode(encoded_text, self.words[key])
                index = self.validate_word(decoded_text)
                key += 1
            print("Hackers most probable word: ", self.words[index])
        return


    def import_words(self):
        file = open("english_words.txt", "r")
        self.words = file.read().splitlines()
        file.close()

    def validate_word(self, word):
        if word.lower() in self.words:
            return self.words.index(word.lower())
        return -1






def pick_cipher():
    print("Type cipher?" + "\n" + "0 = Caesar" + "\n" + \
     "1 = Multiplikativ" + "\n" + "2 = Affine" + "\n" + "3 = Unbreakable" + "\n" + "4 = RSA")
    type_cipher = int(input())
    if type_cipher == 0:
        cipher_1 = Cypher.Caesar()
        cipher_2 = Cypher.Caesar()
        cipher_3 = Cypher.Caesar()
    elif type_cipher == 1:
        cipher_1 = Cypher.Multiplicative()
        cipher_2 = Cypher.Multiplicative()
        cipher_3 = Cypher.Multiplicative()
    elif type_cipher == 2:
        cipher_1 = Cypher.Affine()
        cipher_2 = Cypher.Affine()
        cipher_3 = Cypher.Affine()
    elif type_cipher == 3:
        cipher_1 = Cypher.Unbreakable()
        cipher_2 = Cypher.Unbreakable()
        cipher_3 = Cypher.Unbreakable()
    elif type_cipher == 4:
        cipher_1 = Cypher.RSA()
        cipher_2 = Cypher.RSA()
        cipher_3 = Cypher.RSA()
    return cipher_1, cipher_2, cipher_3


SENDER = Sender()
RECIEVER = Reciever()
CIPHER1, CIPHER2, CIPHER3 = pick_cipher()
SENDER.set_cipher(CIPHER1)
RECIEVER.set_cipher(CIPHER2)
if not isinstance(SENDER.cipher, Cypher.RSA):
    SENDER.operate_cipher()
    RECIEVER.set_encoded_text(SENDER.get_encoded_text())
    RECIEVER.set_key(SENDER.get_key())
    RECIEVER.operate_cipher()
else:
    SENDER.set_key(RECIEVER.cipher.generate_keys())
    SENDER.operate_cipher()
    RECIEVER.set_encoded_text(SENDER.get_encoded_text())
    RECIEVER.set_key(RECIEVER.cipher.secret_key)
    RECIEVER.operate_cipher()

HACKER = Hacker()
HACKER.hack(SENDER.encoded_text, CIPHER3)
input()
