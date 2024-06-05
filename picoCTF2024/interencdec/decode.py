def decode_string(input_string):
    decoded_string = ""
    for char in input_string:
        # Check if the character is a letter
        if char.isalpha():
            # Determine if we need to wrap around the alphabet
            if char.islower():
                decoded_char = chr(((ord(char) - 97 - 7) % 26) + 97)
            else:
                decoded_char = chr(((ord(char) - 65 - 7) % 26) + 65)
        else:
            # If the character is not a letter, leave it unchanged
            decoded_char = char
        decoded_string += decoded_char
    return decoded_string

# Example usage
# input_string = input("Enter the string to encode: ")
input_string = "jhlzhy_k3jy9wa3k_i204hkj6"
decoded_string = decode_string(input_string)
print("Decoded string:", decoded_string)
