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
