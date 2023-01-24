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

# Test
c = CaesarCipher(5)
print(c.encode('chess'))
print(c.decode('BFKKQJX'))
