import socket
import threading

HOST = 'localhost'
PORT = 3300

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#server_socket.setsockopt(socket.SQL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST,PORT))
server_socket.listen()

print('server started listing at {0}:{1}'.format(HOST,PORT))

def client_thread():
    pass

while True:
    
    print('waiting for client')

    client_socket, addr = server_socket.accept()
    new_thread = threading.Thread(target=client_thread)