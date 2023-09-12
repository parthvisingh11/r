import socket
import tqdm
import os
from ntru import *
from util import *

SERVER_HOST = "0.0.0.0"
SERVER_PORT = 5001
BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"

(N, p, q) = (7, 3, 128)
f = poly([-1, 0, 0, 1, 1])
g = poly([0, -1, 0, 1])
h = genPublickey(f, g, N, p, q)

s = socket.socket()
s.bind((SERVER_HOST, SERVER_PORT))
s.listen(10)
print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")
print("Waiting for the client to connect... ")
client_socket, address = s.accept()
print(f"[+] {address} is connected.")
received = client_socket.recv(BUFFER_SIZE).decode()
filename, filesize = received.split(SEPARATOR)
filename = os.path.basename(filename)
filesize = int(filesize)
progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
with open(filename, "wb") as f:
    while True:
        bytes_read = client_socket.recv(BUFFER_SIZE)
        if not bytes_read:
            break
        bytes_read = prepare_decrypt(bytes_read, h, N, p, q)
        f.write(bytes_read)
        progress.update(len(bytes_read))
client_socket.close()
s.close()