import socket

server = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
# The bluetooth adapter address of server device
server.bind(("90:e8:68:53:1d:e2", 4))
server.listen(1)

client, address = server.accept()

try:
    while True:
        data = client.recv(1024)
        if not data:
            break
        print(f"Message: {data.decode('utf-8')}")
        message = input("Enter message: ")
        client.send(message.encode('utf-8'))
except OSError as e:
    print(f"Error: {e}")
    pass
finally:
    client.close()
    server.close()        