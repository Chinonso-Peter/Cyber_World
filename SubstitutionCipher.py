def encrypt(text):
    my_list = []
    for i in range(len(text)):
        # get the corresponding ascii code for each character
        char_pos = ord(text[i])
        # since we are using a positive shift of 3 to encrypt the text we move forward 3 times
        if char_pos > 119:  # edge cases
            new_char_pos = (char_pos - 26) + shift_key
        else:
            new_char_pos = char_pos + shift_key
        # make sure to not overlap or go beyond 122 which is the end of the lower case alphabets in ascii code
        new_char_pos = new_char_pos % 123

        my_list.append(chr(new_char_pos))
    result = ''.join(my_list)
    print(f"Encrypted text is: {result}")
    return result


def decrypt(text):
    my_list = []
    for i in range(len(text)):
        # get the corresponding ascii code for the text
        char_pos = ord(text[i])
        # for decrypting we do reverse of what we did for encrypting
        if char_pos < 100:  # edge cases
            new_char_pos = (char_pos + 26) - shift_key
        else:
            new_char_pos = char_pos - shift_key
        # make sure to not overlap or go beyond 122 which is the end of the lower case alphabets in ascii code
        new_char_pos = new_char_pos % 123
        my_list.append(chr(new_char_pos))
    result = ''.join(my_list)
    print(f"Decrypted text is: {result}")


print("Enter a Text to encrypt")
text = "freeze"
shift_key = 3
enc_text = encrypt(text)
decrypt(enc_text)
