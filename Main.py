import random

letters = list(map(chr, range(33, 123)))

def generate_shift(seed):
    random.seed(seed)
    return [random.randint(1, 255) for _ in range(len(letters))]

def encrypt():
    seed = input("Please enter a password that you will use to decrypt the string: ")
    shifts = generate_shift(seed)

    e_string = input("Please enter a string to encrypt: ").lower()
    encrypted_string = ""

    for i, char in enumerate(e_string):
        if char in letters:
            original_index = letters.index(char)
            new_index = (original_index + shifts[i % len(shifts)]) % len(letters)
            encrypted_string += letters[new_index]
        else:
            encrypted_string += char

    print("Encrypted string:", encrypted_string)

def decrypt():
    seed = input("Please enter the password used for encryption: ")
    expected_shifts = generate_shift(seed)

    encrypted_string = input("Please enter a string to decrypt: ")
    decrypted_string = ""

    for i, char in enumerate(encrypted_string):
        if char in letters:
            encrypted_index = letters.index(char)
            new_index = (encrypted_index - expected_shifts[i % len(expected_shifts)]) % len(letters)
            decrypted_string += letters[new_index]
        else:
            decrypted_string += char

    print("Decrypted string:", decrypted_string)


def main():
    while True:
        choice = input("Choose an option\n1. Encrypt\n2. Decrypt\n3. Exit\n").strip().lower()
        if choice == "e" or choice == "1" or choice == "encrypt":
            encrypt()
        elif choice == "d" or choice == "2" or choice == "decrypt":
            decrypt()
        elif choice == "exit" or choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose again.")

main()
