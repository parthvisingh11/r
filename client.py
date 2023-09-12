import socket
import tqdm
import os
from ntru import *
from util import *

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096

s = socket.socket()
host = "172.20.10.4"
port = 5001
print(f"[+] Connecting to {host}:{port}")
s.connect((host, port))
print("[+] Connected to ", host)
filename = input("File to Transfer : ")
filesize = os.path.getsize(filename)
print(filesize)
s.send(f"{filename}{SEPARATOR}{filesize}".encode())
#file = open(filename, 'wb')

(N, p, q) = (7, 3, 128)
f = poly([-1, 0, 0, 1, 1])
g = poly([0, -1, 0, 1])
h = genPublickey(f, g, N, p, q)

progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
with open(filename, "rb") as f:
    while True:
        bytes_read = f.read(BUFFER_SIZE)
        if not bytes_read:
            break
        bytes_read = prepare_encryp(bytes_read, h, N, p, q)
        temp = listToString(bytes_read)
        s.sendall(temp)
        progress.update(len(bytes_read))
s.close()