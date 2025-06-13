from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import base64

class DESCipher:
    def __init__(self, key):
        # Ensure key is exactly 8 bytes (64 bits)
        self.key = self._adjust_key(key)
    
    def _adjust_key(self, key):
        """Adjust the key to be exactly 8 bytes"""
        if len(key) > 8:
            return key[:8].encode('utf-8')
        elif len(key) < 8:
            return (key + '0' * (8 - len(key))).encode('utf-8')
        return key.encode('utf-8')
    
    def encrypt(self, text):
        """Encrypt the text using DES in ECB mode"""
        cipher = DES.new(self.key, DES.MODE_ECB)
        padded_text = pad(text.encode('utf-8'), DES.block_size)
        return cipher.encrypt(padded_text)
    
    def decrypt(self, encrypted_data):
        """Decrypt the encrypted data using DES in ECB mode"""
        cipher = DES.new(self.key, DES.MODE_ECB)
        decrypted_data = cipher.decrypt(encrypted_data)
        return unpad(decrypted_data, DES.block_size).decode('utf-8')
