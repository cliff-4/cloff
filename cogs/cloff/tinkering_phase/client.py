import socket

s = socket.socket()
host = str(input("host address: "))
port = 9215
s.connect((host, port))
print("Connected")

filename = input(str('name?'))
file = open(filename, 'wb')
file_data = s.recv(1024)
file.write(file_data)
file.close()
