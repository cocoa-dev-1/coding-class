import socket
import threading
import random
import pickle
import time
import os
from datetime import datetime

HOST = 'localhost'
PORT = 30120

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#server_socket.setsockopt(socket.SQL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST,PORT))
server_socket.listen()
game_started = False

client_dic = {}
client_point = {}
client_users = 0

print('server started listing at {0}:{1}'.format(HOST,PORT))

#1. 랜덤한 숫자 추출후 모든 클라이언트로 전달
#2. 클릭 성공시 서버로 결과 전달 -> 해당자를 제외한 모든 클라이언트에 색깔 바꿈
#3. 점수 집계

def client_thread(client_socket, addr):
    global client_users
    global client_dic
    global client_point
    print('Connected addr: {0}:{1}'.format(addr[0],addr[1]))
    client_socket.send((f'user_token:{addr[1]}:').encode())
    k_index = list(client_dic).index(addr[1])
    print(k_index)
    while True:
        try:
            data = client_socket.recv(1024)
            if not data: 
                print('Disconnected by ' + addr[0]+':'+addr[1])
                break
            recive_data = data.decode()
            if recive_data.split(':')[0] == 'user_clicked':
                print(client_point, f'player_{k_index+1}')
                client_point[f'player_{k_index+1}'] += 1
                player_point = client_point[f'player_{k_index+1}']
                for k, v in client_dic.items():
                    if k != addr[1]:
                        v.send((f'other_user:{recive_data.split(":")[1]}:player_{k_index+1}:{player_point}:').encode())

        except ConnectionResetError as e:
            print('Disconnected by ' + addr[0],':',addr[1])
            break
    client_users -= 1
    del client_dic[addr[1]]
    print(client_dic, client_users)
    client_socket.close()

def start_game():
    percentage = 0.00000025
    start_time = datetime.now()
    count_time = start_time
    while True:
        now_time = datetime.now()
        if (now_time - start_time).seconds <= 60:
            random_count = random.random()
            if random_count <= percentage:
                try:
                    ran_coordx = random.randint(0,4)
                    ran_coordy = random.randint(0,4)
                    print(ran_coordx, ran_coordy)
                    #button[(ran_coordx,ran_coordy)].set_image(image_black)
                    #button_click[(ran_coordx,ran_coordy)].config(image = image_black)
                    if ran_coordx <= 4 and ran_coordy <= 4:
                        print(ran_coordx, ran_coordy)
                        for i in client_dic.values():
                            i.send(('rand_coords:'+str(ran_coordx)+str(ran_coordy)+':').encode())
                except Exception as e:
                    print('에러코드 발생:\n', e)
            minus_time = datetime.now()
            if (minus_time-count_time).seconds == 5:
                percentage += 0.00000025
                count_time = minus_time
        else:
            break

    print('game ended')

while True:
    
    print('waiting for client')

    client_socket, addr = server_socket.accept()
    print(client_socket, addr)
    if not game_started:
        client_users += 1
        client_dic[addr[1]] = client_socket
        new_thread = threading.Thread(target=client_thread, args=(client_socket, addr))
        new_thread.daemon = True
        new_thread.start()
        player_index = list(client_dic).index(addr[1])
        client_point[f'player_{player_index+1}'] = 0
        # for k, v in client_dic.items():
        #     if addr[1] != k:
        #         k_index = list(client_dic).index(addr[1])
        #         v.send(f'create_user_label:player_{k_index+1}:'.encode())
        #     else:
        #         for i, j in client_dic.items():
        #             if addr[1] != i:
        #                 k_index = list(client_dic).index(i)
        #                 v.send(f'create_user_label:player_{k_index+1}:'.encode())
        # client_point[f'player_{player_index+1}'] = 0
        if client_users == 4:
            for k, v in client_dic.items():
                k_index = list(client_dic).index(k)
                for i, j in client_dic.items():
                    j.send(f'create_user_label:player_{k_index+1}:{k}:'.encode())
                    time.sleep(0.1)
            time.sleep(0.5)
            print(client_point)
            print('start')
            start_game_th = threading.Thread(target=start_game, args=())
            start_game_th.daemon = True
            start_game_th.start()
            game_started = True
    else:
        client_socket.close()