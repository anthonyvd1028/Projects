import math
from Crypto.Util.number import long_to_bytes

comps = [componet[4:-1] for componet in open('output.txt', 'r').readlines()]

c = int(comps[2], 16)
n = int(comps[1], 16)
x = int(comps[0], 16)

q = (x // 2) + math.isqrt((x // 2) ** 2 - n)
p = x - q
e = 65537
phi_n = (p - 1) * (q - 1)
d = pow(e, -1, phi_n)

decrypted_integer = pow(c, d, n)
decrypted_message_bytes = long_to_bytes(decrypted_integer)

decrypted_message = decrypted_message_bytes.decode('utf-8', errors='ignore')  

print("Decrypted Integer:", decrypted_integer)
print("Decrypted Message:", decrypted_message)