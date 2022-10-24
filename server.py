import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

def handle_client(conn,addr):
    pass


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            data = data.decode()
            if data == 'close':
                print(f'Connection terminated by {addr}')
                break
            print(f'Response from {addr[0]}:',data)
            reply = input(f'Reply to {addr[0]}:')
            conn.sendall(reply.encode())