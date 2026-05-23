# python3

import socket
import time

# Create client socket.
client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server (replace 127.0.0.1 with the real server IP).
client_sock.connect(('172.16.0.2', 6543))

count = 1
while True:
    # Send some data to server.
    client_sock.sendall(f'Hello, world: {count}\n'.encode('utf-8'))

    # Receive some data back.
    chunks = []
    while True:
        data = client_sock.recv(2048)
        if not data:
            break
        chunks.append(data)
    print('Received', repr(b''.join(chunks)))
    count = count + 1
    time.sleep(2)

# Disconnect from server.
client_sock.close()