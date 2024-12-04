#Added another code for demonstration of Encryption algorithm in Cybersecurity called ceaser cipher technique

import random

def text_to_cipher(text, key):
    cipher_text = []

    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            char_index = ord(char) - base
            new_index = (char_index + key) % 26
            cipher_char = chr(base + new_index)
            cipher_text.append(cipher_char)
        else:
            cipher_text.append(char)

    return ''.join(cipher_text)

def cipher_to_text(text, key):
    plain_text = []

    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            char_index = ord(char) - base
            new_index = (char_index - key) % 26
            plain_char = chr(base + new_index)
            plain_text.append(plain_char)
        else:
            plain_text.append(char)

    return ''.join(plain_text)

if __name__ == "__main__":
    plaintext = input("Enter the plain text: ")
    key = random.randint(1, 20)
    print(f"Generated key: {key}")
    result = text_to_cipher(plaintext, key)
    decryptmsg=cipher_to_text(result,key)
    print(f"Cipher text: {result}")
    print(f"The plain text decrypted: {decryptmsg}")
