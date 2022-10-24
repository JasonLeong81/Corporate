import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
SERVER = "192.168.1.84"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    client.send(message)
    print('Server:',client.recv(2048).decode(FORMAT))


while True:
    msg = input('Enter: ')
    send(msg)
    if msg == 'close':
        client.close()
        break
