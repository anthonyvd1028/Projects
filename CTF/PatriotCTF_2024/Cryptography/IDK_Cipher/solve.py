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
