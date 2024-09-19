# Transposition-trial

> Anthony DiTaranto | 8/10/2024

## Description

Our data got corrupted on the way here. Luckily, nothing got replaced, but every block of 3 got scrambled around! The first word seems to be three letters long, maybe you can use that to recover the rest of the message.
Download the corrupted message <ins>here</ins>.


#### message.txt

`heTfl g as iicpCTo{7F4NRP051N5_16_35P3X51N3_V6E5926A}4`

#### Hint

Split the message up into blocks of 3 and see how the first block is scrambled

## Script

[Transposition-trial.py](https://github.com/anthonyvd1028/CTF/blob/main/picoCTF_2022/Cryptography/transposition-trial/transposition-trial.py)

```
cipher = open('message.txt', 'r').read()

character_blocks = [ cipher[i:i + 3] for i in range(0, len(cipher), 3) ]

for i in range(len(character_blocks)):
    character_blocks[i] = character_blocks[i][2] + character_blocks[i][:2]

plaintext = "".join(character_blocks)

print(plaintext)
```

## Flag
`picoCTF{7R4N5P051N6_15_3XP3N51V3_56E6924A}`