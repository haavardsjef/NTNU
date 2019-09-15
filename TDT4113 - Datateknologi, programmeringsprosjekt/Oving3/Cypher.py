"""cypher project, TDT4113, by Håvard Hjelmeseth"""

import random
import crypto_utils


class Cypher:
    """Superklasse"""

    def __init__(self):
        self.alphabet = self.generate_alphabet(65, 90)
        #self.alphabet = self.generate_alphabet(32, 126)
        self.alphabet_size = len(self.alphabet)

    @staticmethod
    def generate_alphabet(start, end):
        """Generates an array of all elements from ascii code start, to ascii code end"""
        temp = []
        for i in range(start, end+1):
            temp.append(chr(i))
        return temp

    def encode(self, text, key):
        """Dummy method, implemented in subclasses"""
        return 0

    def decode(self, encoded_text, key):
        """Dummy method, implemented in subclasses"""
        return 0

    def verify(self, text, key):
        """Checks to see if text is the same ofter encoding, then decoding"""
        temp = self.encode(text, key)
        return text == self.decode(temp, key)

    def generate_keys(self):
        """Generate random keys"""


class Caesar(Cypher):
    """En implementasjon av Cypher som bruker Caeser koding"""

    def __init__(self):
        Cypher.__init__(self)

    def encode(self, text, key):
        encoded_text = ""
        for letter in text:
            encoded_text += self.alphabet[(self.alphabet.index(letter) + key) % self.alphabet_size]
        return encoded_text

    def decode(self, encoded_text, key):
        return self.encode(encoded_text, self.alphabet_size - key)

    def generate_keys(self):
        """Generate random keys"""
        return random.randint(1, self.alphabet_size)


class Multiplicative(Cypher):
    """En implementasjon av Cypher som bruker Multiplikativ koding"""

    def __init__(self):
        Cypher.__init__(self)

    def encode(self, text, key):
        encoded_text = ""
        for letter in text:
            encoded_text += self.alphabet[(self.alphabet.index(letter) * key) % self.alphabet_size]
        return encoded_text

    def decode(self, encoded_text, key):
        return self.encode(encoded_text, crypto_utils.modular_inverse(key, self.alphabet_size))

    def generate_keys(self):
        """Generate random keys"""
        key = False
        while not key:
            temp = random.randint(1, self.alphabet_size)
            if crypto_utils.modular_inverse(temp, self.alphabet_size):
                key = True
        return temp


class Affine(Cypher):
    """En implementasjon av Cypher som bruker Affine koding"""

    def __init__(self):
        Cypher.__init__(self)

    def encode(self, text, key):
        n1, n2 = key
        return self.encode_caesar(self.encode_multiplicative(text, n1), n2)

    def decode(self, encoded_text, key):
        n1, n2 = key
        return self.decode_multiplicative(self.decode_caesar(encoded_text, n2), n1)


    def encode_multiplicative(self, text, key):
        """A straight copy from the method encode in class Multiplicative"""
        encoded_text = ""
        for letter in text:
            encoded_text += self.alphabet[(self.alphabet.index(letter) * key) % self.alphabet_size]
        return encoded_text

    def decode_multiplicative(self, encoded_text, key):
        """A straight copy from the method decode in class Multiplicative"""
        return self.encode_multiplicative(encoded_text, crypto_utils.modular_inverse(key, self.alphabet_size))

    def encode_caesar(self, text, key):
        """A straight copy from the method encode in class Caesar"""
        encoded_text = ""
        for letter in text:
            encoded_text += self.alphabet[(self.alphabet.index(letter) + key) % self.alphabet_size]
        return encoded_text

    def decode_caesar(self, encoded_text, key):
        """A straight copy from the method decode in class Caesar"""
        return self.encode_caesar(encoded_text, self.alphabet_size - key)

    def generate_keys(self):
        """Generate random keys"""
        key = False
        while not key:
            print("Finding key")
            temp = random.randint(1, self.alphabet_size)
            if crypto_utils.modular_inverse(temp, self.alphabet_size):
                key = True
        return temp, random.randint(1, self.alphabet_size)




class Unbreakable(Cypher):
    """En implementasjon av Cypher som bruker Unbreakable koding"""

    def __init__(self):
        Cypher.__init__(self)

    def encode(self, text, key):
        """Encodes using a secret key string"""
        # Figures out which natural number til multiply key
        # with so that we can guarantee that len(key) > len(text)
        extend_factor = (len(text) // len(key)) + 1 # Utv
        extended_key = key * extend_factor
        encoded_text = ""
        i = 0
        for letter in text:
            encoded_text += self.alphabet[(self.alphabet.index(letter) +
                                           self.alphabet.index(extended_key[i])) % self.alphabet_size]
            i += 1
        return encoded_text

    def decode(self, encoded_text, key):
        decode_key = ""
        for letter in key:
            decode_key += self.alphabet[(self.alphabet_size - self.alphabet.index(letter)) % self.alphabet_size]
        return self.encode(encoded_text, decode_key)

class RSA(Cypher):
    """En implementasjon av Cypher som bruker RSA koding"""

    def __init__(self):
        Cypher.__init__(self)
        self.secret_key = None

    def encode(self, text, key):
        n, e = key
        blocks = crypto_utils.blocks_from_text(text, 4)
        encoded_blocks = []
        for block in blocks:
            encoded_blocks.append(pow(block, e, n))
        return encoded_blocks

    def decode(self, encoded_text, key):
        decoded_blocks = []
        n, d = self.secret_key
        for block in encoded_text:
            decoded_blocks.append(pow(block, d, n))
        return crypto_utils.text_from_blocks(decoded_blocks, 16)

    def generate_keys(self):
        """Generate random keys"""
        prime_p = crypto_utils.generate_random_prime(16)
        prime_q = prime_p
        while prime_p == prime_q:
            prime_q = crypto_utils.generate_random_prime(16)
        n = prime_p * prime_q
        phi = (prime_p - 1) * (prime_q - 1)
        d = False
        while not d:
            e = random.randint(3, phi-1)
            d = crypto_utils.modular_inverse(e, phi)
        self.secret_key = (n, d)
        return (n, e)


CIPHER = Affine()
TEXT = input("Encode: ")
KEY = CIPHER.generate_keys()
print(KEY)
X = CIPHER.encode(TEXT, KEY)
print(X)
Y = CIPHER.decode(X, KEY)
print(Y)
print(CIPHER.verify(TEXT, KEY))
input()
