# Winning Factors

> Anthony DiTaranto | 10/18/2024

## Description

As another test of your programming prowess, Turbo Tactical wants to see if you can write a script to solve mathematic equations being served by a remote server within 3 seconds.

## Additional Info 

`147.182.245.126:33001`

## Solution

From the challenge description, we have to solve a mathematic problem from a remote server within 3 seconds. We also get an IP address and a port. With the port and IP address, I decided to enter the command `nc 147.182.245.126 33001`, and was prompted to enter the factorial of a very large number.

Finding and entering this answer would be impossible by hand, so I made a script which retrieves the number, computes the factorial, and finally sends the answer to the remote server. 

Once the server receives my answer to the question, it responds back with the flag. It is important to note that the script sometimes doesn't get the flag if the number is very big, ie 650!.

## solve.py

```
import socket
import math

ip = '147.182.245.126'
port = 33001

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))

while True:
    data = s.recv(1024).decode('utf-8')
    print(data)

    if (data.find('fact')):
        num = int(data.split()[4].strip('.'))
        s.send(str(math.factorial(num)).encode('utf-8'))
    
    print(s.recv(1024).decode('utf-8'))
    s.close()
    break
```

## Flag
`flag{1ntr0_f4ct0r14l_5t3p}`
