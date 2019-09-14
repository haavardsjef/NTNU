

class Cypher:
    """Superklasse"""
    def __init__(self):
        self.alphabet = self.generate_alphabet(32, 126)
        self.alphabet_size = len(self.alphabet)

    def generate_alphabet(self, a, b):
        """Generates an array of all elements from ascii code a, to ascii code b"""
        temp = []
        for i in range(a,b+1):
            temp.append(chr(i))
        return temp

    def encode(self, text):
        pass

    def decode(self, encoded_text):
        pass

    def verify(self, text):
        """Checks to see if text is the same ofter encoding, then decoding"""
        temp = self.encode(text)
        return text == self.decode(temp)

    def generate_keys(self):
        pass

class Caesar(Cypher):
    """En implementasjon av Cypher"""
    def __init__(self, key):
        Cypher.__init__(self)
        self.key = key

    def encode(self, text):
        encoded_text = ""
        for letter in text:
            encoded_text += self.alphabet[(self.alphabet.index(letter)+self.key) % self.alphabet_size]
        return encoded_text

    def decode(self, encoded_text):
        text = ""
        for letter in encoded_text:
            text += self.alphabet[(self.alphabet.index(letter) + self.alphabet_size - self.key) % self.alphabet_size]
        return text

class Multiplicative(Cypher):
    def __init__(self):
        Cypher.__init__(self)

    def encode(self, text):
        pass
        
    def decode(self, text):
        pass




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
        caesar = Caeser(key )
        pass

class Reciever:
    """Subklasse av Person"""
    def operate_cipher(self):
        pass

class Hacker:
    """Subklasse av Person?"""
    pass


cipher = Caesar(2)
text = input("Encode: ")
x = cipher.encode(text)
print(x)
y = cipher.decode(x)
print(y)
print(cipher.verify(text))
input()
