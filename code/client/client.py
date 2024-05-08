import socket
import struct

hote = "localhost"
port = 15555

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((hote, port))
print("Connection on {}".format(port))

data = struct.pack("!HHHH", 120,150,320,25)

socket.send(data)

print("Close")
socket.close()
