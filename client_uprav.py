import socket
from pprint import pprint
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('192.168.1.100',777))
while True:
    try:
        client.send(input("Enter your str: ").encode('utf-8'))
    except Exception:
        print('Ну и ты тупишь братан)')
