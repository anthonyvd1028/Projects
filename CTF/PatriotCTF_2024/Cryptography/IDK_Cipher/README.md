# IDK Cipher

> Anthony DiTaranto | 9/22/2024

## Description

I spent a couple of hours with ???; now I am the world's best cryptographer!!! note: the flag contents will just random chars-- not english/leetspeak

## encode.py

```
import base64
"""
********************************************
*                                          *
*                                          *
********************************************
"""
# WARNING: This is a secret key. Do not expose it.
srt_key = 'secretkey' # // TODO: change the placeholder
usr_input = input("\t:"*10)
if len(usr_input) <= 1:
    raise ValueError("PT must be greater than 1")
if len(usr_input) % 2 != 0:
    raise ValueError("PT can only be an even number")
if not usr_input.isalnum():
    raise ValueError("Only alphabets and numbers supported")
# WARNING: Reversing input might expose sensitive information.
rsv_input = usr_input[::-1]
output_arr = []
for i in range(int(len(usr_input) / 2)):
    c1 = ord(usr_input[i])
    c2 = ord(rsv_input[i])
    enc_p1 = chr(c1 ^ ord(srt_key[i % len(srt_key)]))
    enc_p2 = chr(c2 ^ ord(srt_key[i % len(srt_key)]))
    output_arr.append(enc_p1)
    output_arr.append(enc_p2)
# WARNING: Encoded text should not be decoded without proper authorization.
encoded_val = ''.join(output_arr)
b64_enc_val = base64.b64encode(encoded_val.encode())
R = "R"*20
E = "E"*5
EXCLAMATION = "!"*5
print(f"ULTRA SUPE{R} SECUR{E} Encoded Cipher Text{EXCLAMATION}:", b64_enc_val.decode())
```

## Cipher Text

`QRVWUFdWEUpdXEVGCF8DVEoYEEIBBlEAE0dQAURFD1I=`

## Solution

My first step to solve this cryptography challenge was to analyze how the encryption process works. The `encode.py` does the following:

1. Gets a user input that is even length, has length greater than 1, and contains only letters and numbers and stores it to a variable
2. Makes another variable that is the reverse of the user input
3. Uses a for loop to iterate i from 0 to half the length of the user input -1
4. Gets the decimal representation of position i in the user input and the reverse user input and stores it to variables c1 and c2 respectively
5. Gets the character of the result of c1 being XOR'd against one of the characters in 'secretkey' and stores it to enc_p1
6. Gets the character of the result of c2 being XOR'd against one of the characters in 'secretkey' and stores it to enc_p2
7. Appends enc_p1 and end_p2 to an array in this order
8. Now outside of the for loop, the array with the encrypted characters is joined together
9. The cipher is then Base64 encoded and then outputted

My first step was to turn the Base64 encoded cipher text into hex which I used [CyberChef](https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true,false)To_Hex('Space',0)&input=UVJWV1VGZFdFVXBkWEVWR0NGOERWRW9ZRUVJQkJsRUFFMGRRQVVSRkQxST0). Next, I turned the cipher hex into an array using the python split function.

Inside the for loop, I set the character at position i to enc_p1 and the character at position i + 1 to enc_p2. Then, I got the character of the result from enc_p1 being XOR'd against a character in "secretkey". I did the same for enc_p2.

The character in "secretkey" is being iterated with j instead of i because i is skipping by 2 each loop. This is because the character at position i belongs to the user input while the character at position i + 1 belongs to the reverse user input.

After the XOR is done for both enc_p1 and enc_p2, they are added to strings. After the for loop is done iterating, the string that is for the reverse user input is reversed again and comibined with the string related to the user input. Finally, the flag is wrapped with pctf{} and outputted.

## Script

```
Cipher_base64 = 'QRVWUFdWEUpdXEVGCF8DVEoYEEIBBlEAE0dQAURFD1I='
Cipher_Hex = '41 15 56 50 57 56 11 4a 5d 5c 45 46 08 5f 03 54 4a 18 10 42 01 06 51 00 13 47 50 01 44 45 0f 52'
Cipher_Hex = Cipher_Hex.split(' ')
srt_key = 'secretkey'

first_half = ''
second_half = ''

j = 0
for i in range(0, len(Cipher_Hex) - 1, 2):
    enc_p1 = Cipher_Hex[i]
    enc_p2 = Cipher_Hex[i + 1]

    dec_p1 = chr(int(enc_p1, 16) ^ ord(srt_key[j % len(srt_key)]))
    dec_p2 = chr(int(enc_p2, 16) ^ ord(srt_key[j % len(srt_key)]))

    first_half += dec_p1
    second_half += dec_p2
    j += 1

    

second_half = second_half[::-1]
plaintext = first_half + second_half
print(f'pctf{{{plaintext}}}')
```

## Flag
`pctf{234c81cf3cd2a50d91d5cc1a1429855f}`
