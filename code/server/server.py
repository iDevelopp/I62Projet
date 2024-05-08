import socket
import struct

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('', 15555))

while True:
        socket.listen(5)
        client, address = socket.accept()
        print("{} connected".format( address ))

        data = client.recv(255)
        unpacked_data = struct.unpack("!HHHH", data)
        if unpacked_data != "":
                print(unpacked_data)

print("Close")
client.close()
stock.close()
