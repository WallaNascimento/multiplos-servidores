import socket

HOST = 'localhost'
#Porta para realizar conexão com o controller
PORT = 50002

#Números digitados separados por espaço
mensagem = input("Digite os números inteiros:\nIniciar com 1 para ORDENAR.\nIniciar com 2 para SOMAR.\n")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall(str.encode(mensagem))


data = s.recv(1024)
print('Mensagem de retorno:', data.decode())