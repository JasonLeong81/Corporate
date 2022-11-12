import socket
import pickle
import threading
import joblib
from test_algo import prediction
filename = 'model.sav'

def order(conn):
    # User will provide item code then we will give them a status (order id, date, item code, quantity, email)
    # employee id will not be shown here as it takes time for company to assign tasks
    item_code = None
    email = None
    quantity = None
    reply = 'What would you like to order?'
    conn.sendall(reply.encode())
    while True:
        data = conn.recv(1024)
        data = data.decode()
        if data == '0': # length of packet
            reply = 'Please enter an Item code. For example, B0001.'
            conn.sendall(reply.encode())
            continue
        if data != '0':
            item_code = data
            break
        if data == 'e':
            return 0

    reply = 'Please enter your email for this order: '
    conn.sendall(reply.encode())
    while True:
        data = conn.recv(1024)
        data = data.decode()
        if data == '0':
            reply = 'Please enter your email for this order.'
            conn.sendall(reply.encode())
            continue
        if data != '0':
            email = data
            break
        if data == 'e':
            return 0

    reply = f'Please specify your order quantity for the item {item_code}: '
    conn.sendall(reply.encode())
    while True:
        data = conn.recv(1024)
        data = data.decode()
        if data == '0':
            reply = 'Please specify a quantity for your order.'
            conn.sendall(reply.encode())
            continue
        if data != '0':
            quantity = data
            break
        if data == 'e':
            return 0

    reply = 'Your order has been received. Thank you for your order! Have a great day :)'
    conn.sendall(reply.encode())
    print(item_code,email,quantity)

def check_order_status(conn):
    # give them a status (order id, date, item code, quantity, email,employee id)
    reply = 'Can you please provide your order ID?'
    conn.sendall(reply.encode())
    while True:
        data = conn.recv(1024)
        data = data.decode()
        if data == '0':
            reply = 'Please enter your order ID.'
            conn.sendall(reply.encode())
            continue
        if data != '0':
            if data == '1':
                reply = 'Here is your order status:'
                conn.sendall(reply.encode())
                break
            else:
                reply = f'Sorry, the order id {data} is not found. Please try again.'
                conn.sendall(reply.encode())
        if data == 'e':
            return 0


def Recommend(conn):
    # just run the gradient boosting model
    business_nature = None
    business_product = None
    business_location = None
    reply = 'Can you please state your business nature?'
    conn.sendall(reply.encode())
    while True:
        data = conn.recv(1024)
        data = data.decode()
        if data == '0':
            reply = 'Please enter your business nature.'
            conn.sendall(reply.encode())
            continue
        if data != '0':
            business_nature = data
            break
        if data == 'e':
            return 0

    reply = 'Can you please state your business product?'
    conn.sendall(reply.encode())
    while True:
        data = conn.recv(1024)
        data = data.decode()
        if data == '0':
            reply = 'Please enter the type of product your business provides.'
            conn.sendall(reply.encode())
            continue
        if data != '0':
            business_product = data
            break
        if data == 'e':
            return 0

    reply = 'Can you please state your current business location (city)?'
    conn.sendall(reply.encode())
    while True:
        data = conn.recv(1024)
        data = data.decode()
        if data == '0':
            reply = 'Please enter a location.'
            conn.sendall(reply.encode())
            continue
        if data != '0':
            business_location = data
            break
        if data == 'e':
            return 0
    # run the model here
    pred = prediction(business_location,business_nature,business_product)
    reply = f'Based on our most recent data, we recommend that the product {pred[0]} is most suitable for your profile.'
    conn.sendall(reply.encode())


HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

def run(PORT):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            conn.sendall(b'Hi there! How can I help you?')
            while True:
                data = conn.recv(1024)
                data = data.decode()
                print(f'Response from {addr[0]}:', data)
                if data.strip().lower() == 'order':
                    order(conn)
                elif data.strip().lower() == 'check order status':
                    check_order_status(conn)
                elif data.strip().lower() == 'close':
                    print(f'Connection terminated by {addr}')
                    break
                elif data.strip().lower() == 'recommend':
                    Recommend(conn)
                else:
                    reply = 'I am sorry but I do not have an answer to that.'
                    conn.sendall(reply.encode())



for i in range(5):
    t = threading.Thread(target=run,args=(PORT,))
    t.start()
    PORT += 1