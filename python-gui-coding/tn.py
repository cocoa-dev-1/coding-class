import tkinter
from tkinter.constants import CURRENT
from typing import Collection
from PIL import ImageTk, Image
import os
import threading
import random
import time
import socket
from playsound import playsound
import pickle

#1. 랜덤한 위치에 일정시간동안 두더지가 올라온다.
#2. 두더지를 클릭하면 점수 상승
#3. 시간이 지나면 점점 빠르게 여러마리 올라오는게 필요
#4. 동시 접속 대결 최대 4명
#5. 게임이 끝나고 점수 합산

#두더지는 버튼
#여러 정보들을 보여주는 컴포넌트는 라벨

#버튼
##1. 위치 잡기 5x5 -> 그리드 방식
##2. 이미지 입히기
##3. 동작 연결하기
HOST = '127.0.0.1'
PORT = 30120

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((HOST,PORT))

coords = {}
current_path = os.getcwd()
button = {}
button_click = {}
timer = 1000
score = 0

root = tkinter.Tk()

root.title('테스트 콘솔')
image_hole = ImageTk.PhotoImage(Image.open(current_path+"/white_button3.png"))
image_black = ImageTk.PhotoImage(Image.open(current_path+"/black_button.png"))

# 서버, 클라이언트 통신 펑션
def new_game(client_socket):
    client_socket.send('succes'.encode())
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                print('Disconnected')
                break
            try:
                return_data = data.decode()
                print(return_data)
                if return_data.split(':')[0] == 'rand_coords':
                    if button[(int(return_data.split(':')[1][0]),int(return_data.split(':')[1][1]))].get_image() == image_hole:
                        button[(int(return_data.split(':')[1][0]),int(return_data.split(':')[1][1]))].set_image(image_black)
                elif return_data.split(':')[0] == 'other_user':
                    button[(int(return_data.split(':')[1][0]),int(return_data.split(':')[1][1]))].set_image(image_hole)
            except:
                print(pickle.loads(data))
        except ConnectionResetError as e:
            print('Disconnected')
            break
    client_socket.close()

def play_sound(sound_path):
    playsound(sound_path)

class Button:
    
    def __init__(self):
        self.coord_x = 0
        self.coord_y = 0
        self.image = image_hole
    
    def set_coords(self, x, y):
        self.coord_x = x
        self.coord_y = y
    
    def set_image(self, image):
        self.image = image
        button_click[(self.coord_x,self.coord_y)].config(image=image)
    
    def get_image(self):
        return self.image
    
    def get_coords(self):
        return (self.coord_x, self.coord_y)
    
    def click(self):
        global score
        global my_string_var
        play = threading.Thread(target=play_sound, args=('click_sound.mp3',))
        play.daemon = True
        play.start()
        if self.image == image_black:
            client_socket.send(('user_clicked:'+str(self.coord_x)+str(self.coord_y)).encode())
            self.image = image_hole
            score += 1
            my_string_var.set("내 점수: {0}점".format(score))
            button_click[(self.coord_x, self.coord_y)].config(image=image_hole)

class CreateLabel:
    
    def __init__(self, window, text, width, height, relief, row, col, colspan):
        self.window = window
        self.text = tkinter.StringVar().set(text)
        self.width = width
        self.height = height
        self.relief = relief
        self.row = row
        self.col = col
        self.colspan = colspan
        self.label = tkinter.Label(
            self.window, 
            textvariable=self.text, 
            width=self.width, 
            height=self.height, 
            relief = self.relief
        ).grid(
            row = self.row, 
            column = self.col, 
            columnspan=self.colspan
        )

my_string_var = tkinter.StringVar()
my_string_var.set("내 점수: 0점")
my_label = tkinter.Label(root, text="게임이 시작되었습니다.", width=30, height=5, relief="solid").grid(row=0,column=5, columnspan=2)
my_score = tkinter.Label(root, textvariable = my_string_var, width=30, height=5, relief="solid").grid(row=1,column=5, columnspan=2)



for i in range(5):
    for j in range(5):
        button[(j,i)] = Button()
        button[(j,i)].set_coords(j, i)
        button_click[(j,i)] = tkinter.Button(root, image=image_hole, command=button[(j,i)].click)
        button_click[(j,i)].grid(row=i, column=j)

new_thread = threading.Thread(target=new_game, args=(client_socket,))
new_thread.start()


root.mainloop()




