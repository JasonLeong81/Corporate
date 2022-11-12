import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        d = input('Enter: ')
        if len(d) == 0:
            print('Please enter a message.')
            continue
        s.sendall(f'{d}'.encode())
        data = s.recv(1024)
        if d.strip() == 'close':
            print('You have closed the connection. Have a great day!')
            break
        print(f"Received {data.decode()}")


