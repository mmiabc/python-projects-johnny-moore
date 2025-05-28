def caesar(message, offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''
    
    for char in message:
        if char.lower() in alphabet:
            is_upper = char.isupper()
            index = alphabet.find(char.lower())
            new_index = (index + offset) % 26
            new_char = alphabet[new_index].upper() if is_upper else alphabet[new_index]
            encrypted_text += new_char
        else:
            encrypted_text += char  # keep spaces, punctuation, etc.

    return encrypted_text

if __name__ == "__main__":
    shift = 3
    text = input('What is your message? ')
    encrypted = caesar(text, shift)
    print('Plain text:', text)
    print('Encrypted text:', encrypted)