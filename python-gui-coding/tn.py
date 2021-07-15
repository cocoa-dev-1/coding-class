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

coords = {}
current_path = os.getcwd()
button = {}
button_click = {}
timer = 1000
score = 0
start_array_size = 1000

root = tkinter.Tk()

root.title('테스트 콘솔')
image_hole = ImageTk.PhotoImage(Image.open(current_path+"/python-gui-coding/white_button3.png"))
image_black = ImageTk.PhotoImage(Image.open(current_path+"/python-gui-coding/black_button.png"))

# x, y 값 가져오기
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
    
    def get_coords(self):
        return (self.coord_x, self.coord_y)
    
    def click(self):
        global score
        global my_string_var
        play = threading.Thread(target=play_sound, args=('python-gui-coding/click_sound.mp3',))
        play.start()
        if self.image == image_black:
            self.image = image_hole
            score += 1
            my_string_var.set("내 점수: {0}점".format(score))
            button_click[(self.coord_x, self.coord_y)].config(image=image_hole)

my_string_var = tkinter.StringVar()
my_string_var.set("내 점수: 0점")
my_label = tkinter.Label(root, text="게임이 시작되었습니다.", width=50, height=5, relief="solid").grid(row=0,column=5, columnspan=2)
my_score = tkinter.Label(root, textvariable = my_string_var, width=50, height=5, relief="solid").grid(row=1,column=5, columnspan=2)


for i in range(5):
    for j in range(5):
        button[(j,i)] = Button()
        button[(j,i)].set_coords(j, i)
        button_click[(j,i)] = tkinter.Button(root, image=image_hole, command=button[(j,i)].click)
        button_click[(j,i)].grid(row=i, column=j)

test = 0
old_ran_coordx = 0
old_ran_coordy = 0
while True:
    root.update()
    try:
        ran_coordx = random.randint(0,start_array_size)
        ran_coordy = random.randint(0,start_array_size)
        button[(ran_coordx,ran_coordy)].set_image(image_black)
        button_click[(ran_coordx,ran_coordy)].config(image = image_black)
    except:
        pass
    test += 1
    if test%3000 == 0:
        start_array_size -= 3

# root.mainloop()




