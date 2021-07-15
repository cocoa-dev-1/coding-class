import socket
import threading
import random

HOST = 'localhost'
PORT = 30120

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#server_socket.setsockopt(socket.SQL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST,PORT))
server_socket.listen()

client_dic = {}
client_users = 0

print('server started listing at {0}:{1}'.format(HOST,PORT))

#1. 랜덤한 숫자 추출후 모든 클라이언트로 전달
#2. 클릭 성공시 서버로 결과 전달 -> 해당자를 제외한 모든 클라이언트에 색깔 바꿈
#3. 점수 집계

def client_thread(client_socket, addr):
    global client_users
    global client_dic
    print('Connected addr: {0}:{1}'.format(addr[0],addr[1]))
    
    while True:
        try:
            data = client_socket.recv(1024)
            if not data: 
                print('Disconnected by ' + addr[0],':',addr[1])
                break
            print(data.decode())

        except ConnectionResetError as e:
            print('Disconnected by ' + addr[0],':',addr[1])
            break
    client_users -= 1
    del client_dic[addr[1]]
    print(client_dic, client_users)
    client_socket.close()

def start_game():
    start_array_size = 1000
    test = 0
    while True:
        try:
            ran_coordx = random.randint(0,start_array_size)
            ran_coordy = random.randint(0,start_array_size)
            #button[(ran_coordx,ran_coordy)].set_image(image_black)
            #button_click[(ran_coordx,ran_coordy)].config(image = image_black)
            if ran_coordx < 5 and ran_coordy < 5:
                for i in client_dic:
                    i.send([ran_coordx,ran_coordy].encode())
        except:
            pass
        test += 1
        if test%3000 == 0:
            start_array_size -= 3

while True:
    
    print('waiting for client')

    client_socket, addr = server_socket.accept()
    print(client_socket, addr)
    new_thread = threading.Thread(target=client_thread, args=(client_socket, addr))
    new_thread.start()
    client_users += 1
    client_dic[addr[1]] = client_socket
    print(client_dic,client_users)