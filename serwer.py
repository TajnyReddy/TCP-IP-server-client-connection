import socket
import threading

def klient(conn, id_klienta):
    while 1:
        data = conn.recv(4096)
        decoded=str(data,'utf-8')
        print("Odebrano od klienta {}:".format( id_klienta), decoded)

        for client in clients:
            if client[0] ==  id_klienta:
                continue
            response = "Otrzymałem od klienta {}: {}".format( id_klienta, decoded)
            encoded=bytes(response,'utf-8')
            client[1].send(encoded)
    conn.close()
def akceptuj(socc):
    client_counter = 1
    while 1:
        conn, _ = socc.accept()
        print("Nowe połączenie zaakceptowane od klienta {}.".format(client_counter))

        clients.append((client_counter, conn))

        client_thread = threading.Thread(group=None, target=klient, name = None, args=(conn, client_counter))
        client_thread.start()

        client_counter += 1
def main():
    socc = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0, fileno=None)
    socc.bind(('localhost', 8999))
    socc.listen()

    global clients
    clients = []
    akceptuj(socc)

if __name__ == "__main__":
    main()
