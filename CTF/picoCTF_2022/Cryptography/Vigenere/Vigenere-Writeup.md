# Vigenere

> Anthony DiTaranto | 8/9/2024

## Description

Can you decrypt this message? Decrypt this message using this key "CYLAB".

#### cipher.txt

`rgnoDVD{O0NU_WQ3_G1G3O3T3_A1AH3S_2951c89f}`

#### Key

`CYLAB`

#### Hint

[Vigenere Cipher Wiki](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher)

## Script

[Vigenere Cipher Script](https://github.com/anthonyvd1028/CTF/blob/main/picoCTF_2022/Cryptography/Vigenere/Vigenere.py)

```
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
```

## Flag
`picoCTF{D0NT_US3_V1G3N3R3_C1PH3R_2951a89h}`