'''
Write a class that, when given a string, will return an uppercase string with each letter shifted forward in the alphabet by however many spots the cipher was initialized to.

For example:

c = CaesarCipher(5); # creates a CipherHelper with a shift of five
c.encode('chess') # returns 'HMJXX'
c.decode('BFKKQJX') # returns 'WAFFLES'
If something in the string is not in the alphabet (e.g. punctuation, spaces), simply leave it as is.
The shift will always be in range of [1, 26].



https://en.wikipedia.org/wiki/Caesar_cipher'''
class CaesarCipher:
    def __init__(self, shift):
        self.shift = shift
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz'

    def encode(self, text):
        encoded = ''
        for char in text:
            if char.isalpha():
                char = char.upper()
                shifted_index = (self.alphabet.index(char.lower()) + self.shift) % 26
                encoded += self.alphabet[shifted_index].upper()
            else:
                encoded += char
        return encoded

    def decode(self, text):
        decoded = ''
        for char in text:
            if char.isalpha():
                char = char.upper()
                shifted_index = (self.alphabet.index(char.lower()) - self.shift) % 26
                decoded += self.alphabet[shifted_index].upper()
            else:
                decoded += char
        return decoded

# Test usage
c = CaesarCipher(5)
print(c.encode('chess')) # should print 'HMJXX'
print(c.decode('BFKKQJX')) # should print 'WAFFLES'
