import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket.AF_INET :tell what type of address our socket will be able to interact with; in this case a hostname and a port number
# socket.AF_SYSTEM: use the TCP protocol for our communication.
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
# port can be resued after we stop and restart the application, avoiding any address already in use errors

address = ('127.0.0.1', 8000)

server_socket.bind(address) 
# clients willbe able to use this address to send data to our server, and if we write data to a client,they will see this as the address that it’s coming from

server_socket.listen()

# listen for incoming connections, which will allow clients to connect to our server socket

connection, client_adress = server_socket.accept() # wait for connection
# This method will block until we get a connection and when we do, it will return a connection and the address of the client that connected. 
# The connection is just another socket we can use to read data from and write data to our client

print(f"I have got connection from {client_adress}")