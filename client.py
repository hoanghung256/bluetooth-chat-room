import socket

client = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
# The bluetooth adapter address of server device
client.connect(("90:e8:68:53:1d:e2", 4))

try:
    while True:
        message = input("Enter message: ")
        client.send(message.encode('utf-8'))
        data = client.recv(1024)
        if not data:
            break
        print(f"Message: {data.decode('utf-8')}")
except OSError as e:
    print(f"Error: {e}")
    pass
finally:
    client.close()