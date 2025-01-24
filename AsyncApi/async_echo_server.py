import asyncio
import socket
from asyncio import AbstractEventLoop


async def echo(connection:socket, loop:AbstractEventLoop):
    while data := await loop.sock_recv(connection, 1024): # Loop forever waiting for data from a client connection
        await loop.sock_sendall(connection, data) # Once we have data, send it back to that client.

async def listen_for_connections(server_socket:socket, loop:AbstractEventLoop):
    while True:
        connection, clinet_address = await loop.sock_accept(server_socket)
        connection.setblocking(False)
        print(f"Got connected from client: {clinet_address}")
        asyncio.create_task(echo(connection, loop)) # Whenever we get a connection, create an echo task to listen for client data.


async def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

    server_address = ('127.0.0.1', 8000)
    server_socket.bind(server_address)
    server_socket.setblocking(False)
    server_socket.listen()
    await listen_for_connections(server_socket, asyncio.get_event_loop())

asyncio.run(main())




