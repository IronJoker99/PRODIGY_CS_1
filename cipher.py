def encrypt(text, shift):
    """
    Encrypts the given text using the Caesar cipher algorithm.
    
    Parameters:
        text (str): The text to be encrypted.
        shift (int): The number of positions each letter in the text should be shifted.
    
    Returns:
        str: The encrypted text.
    """
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if the character is an alphabet
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26  # Wrap around if shifted beyond 'z'
                encrypted_text += chr(shifted)
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26  # Wrap around if shifted beyond 'Z'
                encrypted_text += chr(shifted)
        else:
            encrypted_text += char  # If character is not an alphabet, keep it unchanged
    return encrypted_text


def decrypt(text, shift):
    """
    Decrypts the given text using the Caesar cipher algorithm.
    
    Parameters:
        text (str): The text to be decrypted.
        shift (int): The number of positions each letter in the text was shifted during encryption.
    
    Returns:
        str: The decrypted text.
    """
    decrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if the character is an alphabet
            shifted = ord(char) - shift
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26  # Wrap around if shifted beyond 'a'
                decrypted_text += chr(shifted)
            elif char.isupper():
                if shifted < ord('A'):
                    shifted += 26  # Wrap around if shifted beyond 'A'
                decrypted_text += chr(shifted)
        else:
            decrypted_text += char  # If character is not an alphabet, keep it unchanged
    return decrypted_text


def main():
    print("Welcome to the Caesar Cipher program!")
    while True:
        choice = input("Enter 'E' for encryption, 'D' for decryption, or 'Q' to quit: ").upper()
        if choice == 'E':
            message = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift value (a positive integer): "))
            encrypted_message = encrypt(message, shift)
            print("Encrypted message:", encrypted_message)
        elif choice == 'D':
            message = input("Enter the message to decrypt: ")
            shift = int(input("Enter the shift value used for encryption: "))
            decrypted_message = decrypt(message, shift)
            print("Decrypted message:", decrypted_message)
        elif choice == 'Q':
            print("Thank you for using the Caesar Cipher program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 'E', 'D', or 'Q'.")


if __name__ == "__main__":
    main()
