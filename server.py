import socket
import webbrowser
import os

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("192.168.1.100",7777))
server.listen()
print('Server is running...')
while True:
    user,address = server.accept()
    while True:
        data = user.recv(1024).decode(encoding='utf-8').lower()
        print(data)

        if data == 'youtube':
            webbrowser.open("https://www.youtube.com")
        if data == 'horjuntv':
            webbrowser.open("https://www.horjuntv.com.tm")
        if data=='aydym':
            webbrowser.open("https://www.aydym.com/")
        elif data == 'csgo':
            os.startfile("C:/Users/Windows 10/Desktop")
        elif data == 'vs':
            os.startfile("D:/Visual Studio/Microsoft VS Code/Code.exe")
