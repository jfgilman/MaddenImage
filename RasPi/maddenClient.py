import socket
import sys

computer = input("Computer LL_: ")
if computer == '1':
    host = '152.1.138.157'
elif computer == '2':
    host = '152.1.138.158'
elif computer == '3':
    host = '152.1.138.160'
elif computer == '4':
    host = '152.1.138.159'
elif computer == '6':
    host = '192.168.1.14'
elif computer == '7':
    host = '192.168.1.18'
elif computer == '8':
    host = '192.168.1.24'
elif computer == '9':
    host = '192.168.1.30'
else:
    sys.exit("Please enter a valid computer number.")

port = 5560

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

while True:
    command = input("Enter your command: ")
    if command == "KILL":
        # Send KILL command
        s.send(str.encode(command))
        break

    s.send(str.encode(command))
    reply = s.recv(1024)
    print(reply.decode('utf-8'))

s.close()
