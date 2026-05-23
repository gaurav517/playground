# python3

import socket
import time

# Create client socket.
client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server (replace 127.0.0.1 with the real server IP).
client_sock.connect(('172.16.0.2', 6543))

count = 1
with client_sock.makefile('rb') as sock_file:
    try:
        while True:
            message = f'Hello, world: {count}\n'.encode('utf-8')
            client_sock.sendall(message)

            response = sock_file.readline()
            if not response:
                print('Server closed the connection')
                break

            print('Received', response.decode('utf-8').rstrip('\n'))
            count += 1
            time.sleep(2)
    except KeyboardInterrupt:
        pass

# Disconnect from server.
client_sock.close()