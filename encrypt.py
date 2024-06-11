from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os
import base64
import sys

def generate_key(length: int = 32) -> bytes:
    return os.urandom(length)

def encrypt_message(message: str, key: bytes) -> str:
    iv = os.urandom(16)  # Generate a random 16-byte IV
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(message.encode()) + padder.finalize()
    
    encrypted_message = encryptor.update(padded_data) + encryptor.finalize()
    encrypted_message_b64 = base64.b64encode(iv + encrypted_message).decode('utf-8')
    
    return encrypted_message_b64

def main():
    if len(sys.argv) != 2:
        print("Usage: python encrypt.py <message>")
        return
    
    message = sys.argv[1]
    key = generate_key()
    
    encrypted_message = encrypt_message(message, key)
    key_b64 = base64.b64encode(key).decode('utf-8')
    
    print(f"Encrypted message: {encrypted_message}")

if __name__ == "__main__":
    main()
