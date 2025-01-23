import socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

address = ('127.00.1', 8000)
server_socket.bind(address)
server_socket.listen()
# A socket in listen mode allows multiple client connections simultaneously
# we can call socket.accept repeatedly, and each time a client connects we will get a new connection socket to read and write data to and from that client 

connections = []

try:
    while True:
        connection, clinet_address = server_socket.accept()
        print(f"Got connected to clinet : {clinet_address}")
        connections.append(connection)
        for conn in connections:
            buffer = b''
            while buffer[-2:] != b'\r\n':
                data =conn.recv(2)
                if not data:
                    break
                else:
                    print(f"Got data : {data}")
                    buffer += data
            print(f"Total data recieved : {buffer}")
            connection.send(buffer)
finally:
    server_socket.close()

# methods accept and recv block until they receive data
