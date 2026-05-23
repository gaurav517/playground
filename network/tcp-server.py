import socket

serv_sock = socket.socket(
    socket.AF_INET,      # set protocol family to 'Internet' (INET)
    socket.SOCK_STREAM,  # set socket type to 'stream' (i.e. TCP)
    proto=0              # set the default protocol (for TCP it's IP)
)

print(type(serv_sock))   # <class 'socket.socket'>
print(serv_sock.fileno())