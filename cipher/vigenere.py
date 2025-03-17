def vigenere_cipher(text, keyword, mode):
    result = ""
    keyword_length = len(keyword)
    keyword = keyword.upper()
    key_index = 0

    for i, char in enumerate(text):
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            keyword_shift = ord(keyword[key_index % keyword_length]) - ord('A')

            if mode == "decrypt":
                keyword_shift = -keyword_shift  # Reverse the shift for decryption

            char = chr((ord(char) - ascii_offset + keyword_shift) % 26 + ascii_offset)
            key_index+=1
        result += char

    return result

# Get mode
while True:
    print('Do you want to (e)ncrypt or (d)ecrypt?')
    response = input('> ').lower()
    if response.startswith('e'):
        action = 'encrypt'
        break
    elif response.startswith('d'):
        action = 'decrypt'
        break
    print('Please enter the letter e or d.')

print("Enter the message.")
message = input('> ')

print("Enter the keyword.")
keyword = input('> ').upper()

# Perform encryption/decryption
result = vigenere_cipher(message, keyword, action)

# Display the result
print(f"Result: {result}")