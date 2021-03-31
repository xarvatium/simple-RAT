
import socket


TCP_IP = '127.0.0.1'
TCP_PORT = 2004

BUFFER_SIZE = 2048
MESSAGE = "Connected to client...\n"
receiveMessage = "Executing..."


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(str.encode(MESSAGE))
data = s.recv(BUFFER_SIZE)

while True:
    if data:
        print("received data:", data)
        s.send(str.encode(receiveMessage))
        input("")
    else:
        break

s.close()
print("Closed")