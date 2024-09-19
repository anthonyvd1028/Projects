cipher = open('cipher.txt', 'r').read()
key = 'CYLAB'
plaintext = ''

repetitions = len(cipher) // len(key) + 1
key = (key * repetitions)[:len(cipher)]

key_index = 0
for char in cipher:
    if char.isalpha():
        if char.isupper():
            plaintext += chr((ord(char) - ord(key[key_index].upper())) % 26 + 0x41)
        else:
            plaintext += chr((ord(char) - ord(key[key_index].lower())) % 26 + 0x61)
        key_index += 1
    else:
        plaintext += char

print(f'cipher: {cipher}\nplaintext: {plaintext}')