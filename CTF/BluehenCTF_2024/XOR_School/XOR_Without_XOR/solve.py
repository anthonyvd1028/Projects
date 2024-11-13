cipher = 'u_cnfrj_sr_b_34}yd1tt{0upt04lbmb'

characters = [None] * 32
index = 0
for i in cipher:
    characters[(17 * index) % 32] = i
    index += 1

print("".join(characters))