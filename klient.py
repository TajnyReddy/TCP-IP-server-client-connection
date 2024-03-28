import socket
import threading

def wiadomosc(conn):
    while 1:
        message = input()
        encoded=bytes(message,'utf-8')
        conn.send(encoded)
def odpowiedz(conn):
    while 1:
        response = conn.recv(4096)
        decoded=str(response,'utf-8')
        print(decoded)
        print("Wyślij wiadomość:")
def main():
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0,fileno=None)
    conn.connect(('localhost', 8999))

    send_thread = threading.Thread(group=None, target=wiadomosc, name=None, args=(conn,))
    receive_thread = threading.Thread(group=None, target=odpowiedz, name=None, args=(conn,))
    send_thread.start()
    receive_thread.start()

    send_thread.join()
    receive_thread.join()


if __name__ == "__main__":
    print("Wyślij wiadomość:")
    main()