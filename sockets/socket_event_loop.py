import selectors
import socket
from selectors import SelectorKey
from typing import List, Tuple

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_addres = ('127.0.0.1', 8000)
server_socket.bind(server_addres)
server_socket.setblocking(False)
server_socket.listen()

selector = selectors.DefaultSelector()
selector.register(server_socket, events=selectors.EVENT_READ)

while True:
    events : List[Tuple[SelectorKey,int]] = selector.select(timeout=1) # Create a selector that will timeout after 1 second.
    if len(events) == 0:
        print(f"No Event! waiting a bit more")

    for event, _ in events:
        event_socket = event.fileobj # Get the socket for the event, which is stored in the fileobj field.
        if event_socket == server_socket: # If the event socket is the same as the server socket, we know this is a connection attempt.
            connection, clinet_address = server_socket.accept()
            connection.setblocking(False)
            print(f"I got connected to clinet: {clinet_address}")
            selector.register(connection, selectors.EVENT_READ) # Register the client that connected with our selector
        else:
            data = event_socket.recv(1024) # If the event socket is not the server socket, receive data from the client, and echo it back.
            print(f"got some data: {data}")
            event_socket.send(data)

