import socket

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

HOST = 'localhost'
PORT = 12345

server_socket.bind((HOST,PORT))
server_socket.listen(1)

print("Waiting...")

client_socket,client_address = server_socket.accept()

data = client_socket.recv(1024)
input_string = data.decode()

print("Request dari client :",input_string, "IP Client :",client_address)
response = "Jumlah Karakter :" + str(len(input_string))
client_socket.send(response.encode())

client_socket.close()
server_socket.close()