cipher = open('message.txt', 'r').read()

character_blocks = [ cipher[i:i + 3] for i in range(0, len(cipher), 3) ]

for i in range(len(character_blocks)):
    character_blocks[i] = character_blocks[i][2] + character_blocks[i][:2]

plaintext = "".join(character_blocks)

print(plaintext)