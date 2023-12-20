import socket

HOST = 'localhost'
PORT = 50002
PORTORDENA = 50000
PORTSOMA = 50001

#----------------------------------------
def converteString(lista):
    removido = lista.pop(0)
    final = ''
    for i in range(0,len(lista)):
        final = final + str(lista[i])
        final =final + " "
    final = final[:-1]
    return final


def converteLista(string):
    lista = string.split(" ")

    for cont in range(len(lista)):
        lista[cont] = int(lista[cont])

    return lista

def encaminha(lista):
    if lista[0] == 1:
        mensagem = converteString(lista)

        o = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        o.connect((HOST, PORTORDENA))
        o.sendall(str.encode(mensagem))
        data = o.recv(1024)
        received_data = data.decode()
        
            
    elif lista[0] == 2:
        mensagem =         converteString(lista)

        so = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        so.connect((HOST, PORTSOMA))
        so.sendall(str.encode(mensagem))
        data = so.recv(1024)
        received_data = data.decode()

    else:
        received_data = "Error"
        
    return received_data 
#--------------------------------------

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
    lista = converteLista(received_data)
    final_data = encaminha(lista)

    print(final_data) 
    conn.sendall(str.encode(final_data))    