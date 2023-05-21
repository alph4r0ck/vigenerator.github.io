from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def generate_passphrase(keyword, word_list, aes_key):
    keyword = keyword.lower()
    passphrase = ""

    # Repeat keyword to match the length of word_list
    keyword_repeated = (keyword * (len(word_list) // len(keyword))) + keyword[:len(word_list) % len(keyword)]

    for i in range(len(word_list)):
        keyword_char = keyword_repeated[i]
        keyword_char_value = ord(keyword_char) - ord('a')

        # Get the word from the word_list
        word = word_list[i]

        # Apply Vigenere cipher to each character in the word
        encrypted_word = ""
        for char in word:
            if char.isalpha():
                char_value = (ord(char.lower()) - ord('a') + keyword_char_value) % 26
                encrypted_word += chr(char_value + ord('a'))
            else:
                encrypted_word += char

        passphrase += encrypted_word + " "

    # AES encryption
    cipher = AES.new(aes_key.encode(), AES.MODE_ECB)
    encrypted_passphrase = cipher.encrypt(pad(passphrase.strip().encode(), 16))

    return encrypted_passphrase.hex()


# Example usage
word_list = ["apple", "banana", "carrot", "dog", "elephant", "fish"]
aes_key = "thisisaeskey1234"

# User input for the Vigenere cipher keyword
keyword = input("Enter the keyword for the Vigenere cipher: ")

secure_passphrase = generate_passphrase(keyword, word_list, aes_key)
print(secure_passphrase)
