import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
address = ('127.0.0.1', 8000)
server_socket.bind(address)

server_socket.listen()

try:
    connection, client_address = server_socket.accept() # it waits for connections
    print(f"Got connected to client: {address}")
    buffer = b''
    while buffer[-2:] != b'\r\n': # break condition in telnet
        data = connection.recv(2)
        if not data:
            break
        else:
            print(f"I got data : {data}")
            buffer += data
    print(f"All data is: {buffer}")
    connection.sendall(buffer) # it will send data to client

finally:
    server_socket.close()