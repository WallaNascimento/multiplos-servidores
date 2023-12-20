import socket

HOST = 'localhost'
PORT = 50000

#----------------------------------------
def ordena(lista):
    lista = lista.split(" ")

    for i in range(len(lista)):
        lista[i] = int(lista[i])

    lista.sort()
    final = ''
    
    for i in range(0,len(lista)):
        final = final + str(lista[i])
        final = final + " "

    return final
#    -----------------------------------
    

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
         
    final_data = ordena(received_data)
    
    print(final_data)
    conn.sendall(str.encode(final_data))