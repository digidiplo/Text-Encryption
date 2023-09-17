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

