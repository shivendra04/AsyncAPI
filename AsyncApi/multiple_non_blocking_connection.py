import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

address = ('127.0.0.1', 8000)
server_socket.bind(address)
server_socket.listen()
server_socket.setblocking(False)

connections = []

try:
    while True:
        try:
            connection, client_address = server_socket.accept()
            print(f"connected to the clinet : {client_address}")
            connection.setblocking(False)
            connections.append(connection)
        except BlockingIOError:
            pass
        
        for conn in connections:
            try:
                buffer = b''
                while buffer[-2:] != b'\r\n':
                    data = conn.recv(2)
                    if not data:
                        break
                    else:
                        print(f"got data : {data}")
                        buffer += data
            
                print(f"complete data: {buffer}")
                conn.send(buffer)
            except BlockingIOError:
                pass

finally:
    server_socket.close()

