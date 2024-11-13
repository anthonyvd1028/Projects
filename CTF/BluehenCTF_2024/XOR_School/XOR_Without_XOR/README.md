# XOR without XOR

> Anthony DiTaranto | 11/13/2024

## Description

This is how XOR makes me feel.

This series of problems is called the XOR SCHOOL. For whatever reason I just love xor problems and over the years there are many that have charmed my soul. This sequence is an homage to the many many ways that xor shows up in CTFs. I hope you can see some of the beauty that I see through them.

## Extra Information

```
In [15]: (flag*32)[::17][:32]
Out[15]: u_cnfrj_sr_b_34}yd1tt{0upt04lbmb
```

## solve.py

```
cipher = 'u_cnfrj_sr_b_34}yd1tt{0upt04lbmb'

characters = [None] * 32
index = 0
for i in cipher:
    characters[(17 * index) % 32] = i
    index += 1

print("".join(characters))
```

## Solution

So to solve this challenge, we should first figure out what is happening. In the code snippet, `In [15]: (flag*32)[::17][:32]`, the flag variable is first being repeated 32 times, then every 17th character, i.e., 1st, 18th, etc., is being captured, and finally the output is limited to 32 characters.

I made a [solve.py](https://github.com/anthonyvd1028/Projects/tree/main/CTF/BluehenCTF_2024/XOR_School/XOR_Without_XOR/solve.py) script that first makes an empty list with 32 indexes, and I initialize index to 0. Next, I iterate throughout the scrambled text and put the scrambled character in an array in the correct index, which lets me join the list together at the end.

To unscramble the cipher, I multiply the index variable, which is the original spot in the plaintext, by 17 and then mod the result by 32. This gives us the index of where the scrambled character should be, so we populate the characters list with the unscrambled characters, which we can then use the join Python function to give us the flag.

## Flag
`udctf{just_4_b4by_1ntr0_pr0bl3m}`
