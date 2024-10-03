# XNOR

> Anthony DiTaranto | 9/28/2024

## Description

XNOR! It's like XOR, but it's actually the complete opposite.

## xnor.py

```
import os


def xnor_bit(a_bit, b_bit):
    if a_bit == "1" and b_bit == "1":
        return "1"
    elif a_bit == "1" and b_bit == "0":
        return "0"
    elif a_bit == "0" and b_bit == "1":
        return "0"
    elif a_bit == "0" and b_bit == "0":
        return "1"


def xnor_byte(a_byte, b_byte):
    a_bits = get_bits_from_byte(a_byte)
    b_bits = get_bits_from_byte(b_byte)

    result_bits = [xnor_bit(a_bits[i], b_bits[i]) for i in range(8)]
    result_byte = get_byte_from_bits(result_bits)
    return result_byte


def xnor_bytes(a_bytes, b_bytes):
    assert len(a_bytes) == len(b_bytes)

    return bytes([xnor_byte(a_bytes[i], b_bytes[i]) for i in range(len(a_bytes))])


def get_bits_from_byte(byte):
    return list("{:08b}".format(byte))


def get_byte_from_bits(bits):
    return int("".join(bits), 2)


message = b"Blue is greener than purple for sure!"
key = os.urandom(37)

flag = b"bctf{???????????????????????????????}"


def main():
    print(f"Key: {key.hex()}")
    print(f"\nMessage: {message}")

    encrypted = xnor_bytes(message, key)
    print(f"Enrypted message: {encrypted.hex()}")

    print(f"\nFlag: {flag}")
    encrypted_flag = xnor_bytes(flag, key)
    print(f"Encrypted flag: {encrypted_flag.hex()}")


if __name__ == "__main__":
    main()
```

## xnor_output.txt

```
Key: [[REDACTED]]

Message: b'Blue is greener than purple for sure!'
Enrypted message: fe9d88f3d675d0c90d95468212b79e929efffcf281d04f0cfa6d07704118943da2af36b9f8

Flag: [[REDACTED]]
Encrypted flag: de9289f08d6bcb90359f4dd70e8d95829fc8ffaf90ce5d21f96e3d635f148a68e4eb32efa4
```

## Solution

In this challenge, it takes a twist on the XOR encryption method. In our case we XNOR bits, meaning if they are the same, we return 1, and we return 0 if they aren't the same. We are given a byte string called Message, the encrypted message in hex, and the encrypted flag in hex. The flag and key are both REDACTED.

Our Steps to solve this challenge is going to be:
1. Convert both the message and encrypted message to bits
2. XNOR the message and encrypted message to get the key
3. covert the encrypted flag to bits
4. XNOR the encrypted flag bits with the key
5. Turn the unencrypted flag bits into human readable text

To turn the hex and byte strings into bits, I used the python format function with with either {:08b} or {:04b} for the byte string and hex strings respectively. 

```
for i in range(296):
    a_bit = Message_bits[i]
    b_bit = Encrypted_message_bits[i]
    key += xnor_bit(a_bit, b_bit)
```

Above is the for loop that XNOR's the bits. It gets the bit at position i from the message bits and encrypted message bits and uses the xnor_bit function from xnor.py. 

```
for i in range(296):
    flag += xnor_bit(Encrypted_flag_bits[i], key[i])
```

Above is the for loop that XNOR's the encrypted flag bits with the key, which will give us the flag.

## solve.py

```
Message = b'Blue is greener than purple for sure!'
Encrypted_message = 'fe9d88f3d675d0c90d95468212b79e929efffcf281d04f0cfa6d07704118943da2af36b9f8'
Encrypted_flag = 'de9289f08d6bcb90359f4dd70e8d95829fc8ffaf90ce5d21f96e3d635f148a68e4eb32efa4'
Message_bits = ''
Encrypted_message_bits = ''
Encrypted_flag_bits = ''
key = ''
flag = ''

def xnor_bit(a_bit, b_bit):
    if a_bit == "1" and b_bit == "1":
        return "1"
    elif a_bit == "1" and b_bit == "0":
        return "0"
    elif a_bit == "0" and b_bit == "1":
        return "0"
    elif a_bit == "0" and b_bit == "0":
        return "1"

def bits_to_text(bits):
    result = ''
    for i in range(0, len(bits), 8):
        result += chr(int(flag[i:i+8],2))
    return result


for i in Message:
    Message_bits += "{:08b}".format(i)

for i in Encrypted_message:
    Encrypted_message_bits += "{:04b}".format(int(i, 16))

for i in Encrypted_flag:
    Encrypted_flag_bits += "{:04b}".format(int(i, 16))

for i in range(296):
    a_bit = Message_bits[i]
    b_bit = Encrypted_message_bits[i]
    key += xnor_bit(a_bit, b_bit)
    

for i in range(296):
    flag += xnor_bit(Encrypted_flag_bits[i], key[i])

print(bits_to_text(flag))
```

## Flag
`bctf{why_xn0r_y0u_b31ng_so_3xclu51v3}`
