import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('icio.us', 80))

cmd = 'GET http://icio.us/HTTP/1.0\r\n\n'.encode()

mysock.send(cmd)
while True :
    data=mysock.recv(512)
    if len(data) <1:
        break
    print(data.decode(),end='')
mysock.close()