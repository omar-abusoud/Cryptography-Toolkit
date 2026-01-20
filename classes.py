from dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass
class Cipher(ABC):

    @abstractmethod
    def encrypt(self, plaintext: str) -> str:
        pass

    @abstractmethod
    def decrypt(self, ciphertext: str) -> str:
        pass

@dataclass
class CaesarCipher(Cipher):

    shift: int = 5 # default shift is 5

    def encrypt(self, plaintext: str) -> str:
        result = ""
        for char in plaintext:
            if char.isalpha():
                shift_base = ord('a') if char.islower() else ord('A')
                result += chr((ord(char) - shift_base + self.shift) % 26 + shift_base)
            else:
                result += char
        return result

    def decrypt(self, ciphertext: str) -> str:
        result = ""
        for char in ciphertext:
            if char.isalpha():
                shift_base = ord('a') if char.islower() else ord('A')
                result += chr((ord(char) - shift_base - self.shift) % 26 + shift_base)
            else:
                result += char
        return result

@dataclass
class ROT13Cipher(Cipher):

    def encrypt(self, text):
        result = []
        for c in text:
            if c.isalpha():
                base = ord('A') if c.isupper() else ord('a')
                result.append(chr((ord(c) - base + 13) % 26 + base))
            else:
                result.append(c)
        return ''.join(result)
    
    decrypt = encrypt  # ROT13 is symmetric cipher

@dataclass
class XORCipher(Cipher):

    key: str

    def encrypt(self, text):
        return ''.join(chr(ord(c) ^ ord(self.key[i % len(self.key)])) for i, c in enumerate(text))

    decrypt = encrypt  # XOR is symmetric cipher

@dataclass
class AtbashCipher(Cipher):

    def encrypt(self, plaintext: str) -> str:
        result = ""
        for char in plaintext:
            if char.isalpha():
                shift_base = ord('a') if char.islower() else ord('A')
                result += chr(shift_base + (25 - (ord(char) - shift_base)))
            else:
                result += char
        return result

    decrypt = encrypt  # Atbash is symmetric cipher

class BinaryConverter(Cipher):

    def encrypt(self, text: str) -> str:
        result = ' '.join(format(ord(c), '08b') for c in text)
        return result

    def decrypt(self, binary: str) -> str:
        binary = binary.replace(" ", "") 
        result = ''.join(chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8))
        return result

@dataclass
class Translator(Cipher): # morse code , bacon cipher 
    mapping: dict
    kind : str

    def encrypt(self, text:str) -> str :
        result = []
        for char in text:
            result.append(self.mapping[char] if char in self.mapping else char)

        return ' '.join(result)
    
    def decrypt(self, code:str) -> str :
        result = []
        parts = code.split(" ")
        for symbol in parts:
            if symbol == "" or symbol == "/":   
                result.append(" ")
                continue
            result.append(self.mapping[symbol] if symbol in self.mapping else symbol)
        return ''.join(result)