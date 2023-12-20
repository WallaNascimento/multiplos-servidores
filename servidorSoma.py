import socket
HOST = 'localhost'
PORT = 50001

#----------------------------------------
def soma(lista):
    lista = lista.split(" ")
    auxiliar=0
    for i in range(len(lista)):
        lista[i] = int(lista[i])
        auxiliar = auxiliar + lista[i]
      
    return str(auxiliar)
    #-----------------------------------
    

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen()
print('Aguardando conexao de um cliente')
conn, ender = s.accept()

print('Conectador em', ender)
while True:
    data = conn.recv(1024)
    if not data:
        print('Fechando a conexão')
        conn.close()
        break
    received_data = data.decode()
    final_data = ''
    
    final_data = soma(received_data)

    print(final_data)
    conn.sendall(str.encode(final_data))
    