import os
from cryptography.fernet import Fernet

def generate_key() -> None:
    key = Fernet.generate_key()
    with open('key.txt', 'wb') as key_file:
        key_file.write(key)
    print("[+] Key generated and saved to 'key.txt'")

def load_key() -> bytes:
    if not os.path.exists('key.txt'):
        raise FileNotFoundError("Key file 'key.txt' not found.")
    with open('key.txt', 'rb') as key_file:
        return key_file.read()

def encrypt_file() -> None:
    input_path = 'encrypt.txt'
    output_path = 'decrypt.txt'
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file '{input_path}' not found.")

    key = load_key()
    fernet = Fernet(key)
    with open(input_path, 'rb') as infile:
        data = infile.read()
    encrypted = fernet.encrypt(data)

    with open(output_path, 'wb') as outfile:
        outfile.write(encrypted)
    print(f"[+] File encrypted and saved to '{output_path}'")

def decrypt_file() -> None:
    input_path = 'decrypt.txt'
    output_path = 'decrypted_output.txt'
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file '{input_path}' not found.")

    key = load_key()
    fernet = Fernet(key)
    with open(input_path, 'rb') as infile:
        data = infile.read()
    decrypted = fernet.decrypt(data)

    with open(output_path, 'wb') as outfile:
        outfile.write(decrypted)
    print(f"[+] File decrypted and saved to '{output_path}'")

def menu():
    print("""
=== File Encryption/Decryption Tool ===
1. Generate new key
2. Encrypt 'encrypt.txt' to 'decrypt.txt'
3. Decrypt 'decrypt.txt' to 'decrypted_output.txt'
4. Exit
""")

def main():
    while True:
        menu()
        choice = input("Enter your choice (1-4): ").strip()

        try:
            if choice == '1':
                generate_key()
            elif choice == '2':
                encrypt_file()
            elif choice == '3':
                decrypt_file()
            elif choice == '4':
                print("Exiting. Goodbye!")
                break
            else:
                print("Invalid option. Please choose a number between 1 and 4.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    main()
