import tkinter
from typing import Collection
from PIL import ImageTk, Image
import os

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

root = tkinter.Tk()
root.title('테스트 콘솔')
image_hole = ImageTk.PhotoImage(Image.open("white_button3.png"))
image_black = ImageTk.PhotoImage(Image.open("black_button.png"))

# x, y 값 가져오기
def click():
    print('false')

class Button:
    
    def __init__(self):
        self.coord_x = 0
        self.coord_y = 0
        self.image = image_hole
    
    def set_coords(self, x, y):
        self.coord_x = x
        self.coord_y = y
    
    def get_coords(self):
        return (self.coord_x, self.coord_y)
    
    def click(self):
        print(self.coord_x, self.coord_y)
        

for i in range(5):
    for j in range(5):
        button = Button()
        button.set_coords(j, i)
        button_click = tkinter.Button(root, image=image_hole, command=button.click)
        button_click.grid(row=j, column=i)
        



root.mainloop()

