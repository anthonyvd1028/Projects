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