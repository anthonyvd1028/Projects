# The Moth Flies at Dawn

> Anthony DiTaranto | 10/25/2024

## Description

NICC is on the hunt for the elusive moth-man! In order to draw him out of hiding, we need to cook a nice breakfast for him. Luckily, one of our agents has recovered a hash of the cryptid's favorite breakfast. Crack the hash and serve up a great breakfast!

## Hint

It would be a SHAme if all 256 of these meals went to waste.

## hash.txt

`6c3f70f58c01dac2c14522e18d6ca4e89b9f2b4b3516903329fb36a04cf72c62`

## Solution

From the hint and description, I see that we need to submit the breakfast item that gives us the hash that is inside hash.txt. You could make a python script that iterates throughout the wordlist, hashes the word, and compares it to the original hash. Since the wordlist contained simple words, I decided that it would be easier to use a rainbow table to crack the hash. I used a [website](https://crackstation.net/) with `6c3f70f58c01dac2c14522e18d6ca4e89b9f2b4b3516903329fb36a04cf72c62` as the input and got `blueberrypancake` as the result.

## Flag

`NICC{blueberrypancake}`