# Sum-O-Primes

> Anthony DiTaranto | 8/13/2024

## Description

We have so much faith in RSA we give you not just the product of the primes, but their sum as well!

#### output.txt

```
x = 1626a189dcb38ca6b8e9ee26623ab5c3c6cd7e4c7ff6726f4b03831ca48c617a056827c5763458d0aa7172650072b892649cc73f943f156b795ff5dd2fc9a53b140cf9c3ee2cbb8181d17bb0275f404b4090766f798ad156db7e71000e93db65f3e1bc7406532d0f509fbecf095ef215b4ad51f5e8ac765861e5f93808948bf72
n = 720d66204ec312d7f1bc688495d4585ec58520170b86ed3488c3f9c76407b7e9e466b82a282ba90d484698160f2e27f413b07cf8805d560abdffa977547d5fec3190a1ce284dfc8e92193f2f70590bf9c6e6d0ab449e35ef43ed20232b7f8686696125cde1f950230fbc6858392a3715c1b8a4947748b7fadd5cc921716ad5e0129c91ea88fceee140fb1c594606186afacb69143ef8f7b3b1aa2cc3206395c60e71ec0555dd15838d8a8395e8ccf9a4e4c4199ae0ab3f8af7ebc6605edc5ddd480be2d6c41e38618eba5822a1e566080877268802750de71e890ac865ebf87fdc290d9151e407dff4c97390c9e7388fd538e2716515cea2240f55963c2e0c21
c = 554b90eb12fbece709d7bf23ab91f9b52d71cd77fbf42f65d68623c2055d99956b9bcf2eaf14771fa5781fae86624e44b452a0f68768849faba1b9695ce353a17238a3e7040ee7aede68b35bf4b51daf0982653910b280ac98aad9a5b3c49d226e10b2e8660effc2cb2a553039bde527e42f1795bc078af6ed2928505be6df1ebe993f2ed8c10477dd5cc9f899d1e69b6512b71c732472dde521f5393c76b2f9fbed668560d4e50ca177dd14b923414549d688b20fab94dba7cad7b5a729941c772dc4a1db79b0e6a111d2d2e8998b4e2a272dc940a9dd4cf856faa5a2ee0cb6f36f0ce6edbb421697e517a4d589cc5a880eecf6fbf65e5f6a1a437b06e5ff9a
```

#### Hint

I love squares :)

## Script

[Sum-O-Primes](https://github.com/anthonyvd1028/CTF/blob/main/picoCTF_2022/Cryptography/Sum-O-Primes/Sum-O-Primes.py)

```
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
```

## Flag
`picoCTF{pl33z_n0_g1v3_c0ngru3nc3_0f_5qu4r35_92fe3557}`