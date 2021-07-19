import socket
import threading
import random
import pickle
import time

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
class Timer:

    def __init__(self, time_set):
        self.time_set = time_set
    
    def start(self):
        while self.time_set > 0:
            time.sleep(1)
            self.time_set -= 1
    
    def get_current_time(self):
        return self.time_set


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
            recive_data = data.decode()
            if recive_data.split(':')[0] == 'user_clicked':
                for k, v in client_dic.items():
                    if k != addr[1]:
                        v.send(('other_user:'+recive_data.split(':')[1]).encode())

        except ConnectionResetError as e:
            print('Disconnected by ' + addr[0],':',addr[1])
            break
    client_users -= 1
    del client_dic[addr[1]]
    print(client_dic, client_users)
    client_socket.close()

def start_game():
    start_array_size = 5.0
    test = 0
    new_game_timer = Timer(60)
    new_game_start = threading.Thread(target=new_game_timer.start, args=())
    new_game_start.daemon = True
    new_game_start.start()
    while new_game_timer.get_current_time() > 0:
        print(start_array_size)
        if start_array_size > 0.0:
            time.sleep(start_array_size)
        else:
            time.sleep(0.2)
        try:
            ran_coordx = random.randint(0,4)
            ran_coordy = random.randint(0,4)
            print(ran_coordx, ran_coordy)
            #button[(ran_coordx,ran_coordy)].set_image(image_black)
            #button_click[(ran_coordx,ran_coordy)].config(image = image_black)
            if ran_coordx <= 4 and ran_coordy <= 4:
                print(ran_coordx, ran_coordy)
                for i in client_dic.values():
                    i.send(('rand_coords:'+str(ran_coordx)+str(ran_coordy)).encode())
        except:
            pass
        if start_array_size > 0.0:
            if start_array_size > 1.0:
                start_array_size -= 0.5
            else:
                start_array_size -= 0.2
        start_array_size = round(start_array_size, 1)
    print('game ended')

while True:
    
    print('waiting for client')

    client_socket, addr = server_socket.accept()
    print(client_socket, addr)
    new_thread = threading.Thread(target=client_thread, args=(client_socket, addr))
    new_thread.start()
    client_users += 1
    client_dic[addr[1]] = client_socket
    print(client_dic,client_users)
    if client_users == 1:
        print('start')
        start_game_th = threading.Thread(target=start_game, args=())
        start_game_th.daemon = True
        start_game_th.start()