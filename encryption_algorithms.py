def caesar_cipher(text, shift):
    encrypted_text = ""

    # run through length of text
    for i in range(len(text)):
        char = text[i]

        # encrypt uppercase letters
        if (char.isupper()):
            encrypted_text += chr((ord(char) + shift-65) % 26 + 65)
        
        # encrypt lowercase
        else:
            encrypted_text += chr((ord(char) + shift-97) % 26 + 97)
    
    return encrypted_text

def reverse_caeser(text, shift):
    decrypted_text = ""

    # run through length of text
    for i in range(len(text)):
        char = text[i]

        # encrypt uppercase letters
        if (char.isupper()):
            decrypted_text -= chr((ord(char) + shift-65) % 26 + 65)

        # encrypt lowercase
        else:
            decrypted_text += chr((ord(char) + shift-97) % 26 + 97)
    
    return decrypted_text

# Python code to implement
# Vigenere Cipher

# This function generates the
# key in a cyclic manner until
# it's length isn't equal to
# the length of original text
def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return(key)
    else:
        for i in range(len(string) -
                    len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))
        
    # This function returns the
    # encrypted text generated
    # with the help of the key
def cipherText(string, key):
    cipher_text = []
    for i in range(len(string)):
        x = (ord(string[i]) +
            ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    return("" . join(cipher_text))
    
# This function decrypts the
# encrypted text and returns
# the original text
def originalText(cipher_text, key):
    orig_text = []
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) -
             ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return("" . join(orig_text))
     
# Driver code
if __name__ == "__main__":
    string = "GEEKSFORGEEKS"
    keyword = "AYUSH"
    key = generateKey(string, keyword)
    cipher_text = cipherText(string,key)
    print("Ciphertext :", cipher_text)
    print("Original/Decrypted Text :",
           originalText(cipher_text, key))
