from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from os import urandom

# Function to encrypt a file
def encrypt_file(file_path, key, iv):
    # Open the file to be encrypted
    with open(file_path, 'rb') as f:
        data = f.read()

    # Pad the data to make it a multiple of the block size (16 bytes for AES)
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(data) + padder.finalize()

    # Create a cipher object using the key and iv
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    # Encrypt the data
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

    # Save the encrypted file
    with open(file_path + '.enc', 'wb') as enc_file:
        enc_file.write(iv + encrypted_data)

# Generate a random 32-byte key and 16-byte IV
key = urandom(32)  # 32 bytes = 256 bits (AES-256)
iv = urandom(16)   # 16 bytes (AES block size)

# Call the encrypt_file function
encrypt_file('path_to_file.txt', key, iv)
from cryptography.hazmat.primitives import padding

# Function to decrypt a file
def decrypt_file(file_path, key):
    # Open the encrypted file
    with open(file_path, 'rb') as enc_file:
        data = enc_file.read()

    # Extract the IV (first 16 bytes) and the encrypted data
    iv = data[:16]
    encrypted_data = data[16:]

    # Create a cipher object using the key and iv
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    # Decrypt the data
    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()

    # Unpad the decrypted data
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    original_data = unpadder.update(decrypted_data) + unpadder.finalize()

    # Save the decrypted file
    with open(file_path.replace('.enc', '_decrypted.txt'), 'wb') as dec_file:
        dec_file.write(original_data)

# Call the decrypt_file function
decrypt_file('path_to_file.txt.enc', key)
