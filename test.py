import socket
import threading

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
print(SERVER)
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    while connected:
        data = conn.recv(1024)  # 1024 bytes
        if data.decode(FORMAT) == 'close':
            conn.send(b'Bye Bye!')
            connected = False
            print(f'Client {addr[0]} has ended connection.')
            continue
        conn.send(b'Message Received.')
    conn.close()

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept() # waits until a new connection occurs
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        stop = input('Shut down server (y/n)? ')
        if stop == 'y':
            server.close()
            break
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("[STARTING] server is starting...")
start()