import socket

serv_sock = socket.socket(
    socket.AF_INET,      # set protocol family to 'Internet' (INET)
    socket.SOCK_STREAM,  # set socket type to 'stream' (i.e. TCP)
    proto=0              # set the default protocol (for TCP it's IP)
)

print(type(serv_sock))   # <class 'socket.socket'>
print(serv_sock.fileno())

# bind to network interface (''/'0.0.0.0' means all interfaces) and port
serv_sock.bind(('0.0.0.0', 6543))

# listen
backlog = 10 # max number of established connections waiting for acceptance
serv_sock.listen(backlog)

print('server: ', serv_sock.getsockname())

while True:
    client_sock, client_addr = serv_sock.accept()
    print('New connection from', client_addr)

    print('printing peer:')
    client_sock.getpeername()

    chunks = []
    while True:
        data = client_sock.recv(2048)
        if not data:
            break
        chunks.append(data)
    client_sock.sendall(b''.join(chunks))
    client_sock.close()

