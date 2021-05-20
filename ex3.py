user_name = input("이름을 입력하세요")
while True:
    user_job = input("직업을 입력하세요(마법사, 검사)")
    if user_job not in ['마법사', '검사']:
        print('잘못된 직업명 입니다.')
    else:
        break
user_level = 1
user_hp = 100
user_mp = 100
user_utils = {'마법사': {'스킬': ('화염구', '속박'), '소지품': ('지팡이', '팔목 보호대', '귀걸이')}, 
'검사': {'스킬':('휘두르기', '내리꽂기'), '소지품': ('검', '갑주', '허리띠')}}

while True:
    print("아래의 메뉴를 선택해 주세요")
    print("1. 정보")
    print("1. 스킬")
    print("3. 소지품")
    print("4. 나가기")
    menu_sel = int(input("번호를 입력하세요."))
    if menu_sel == 1:
        print(user_level)
        print(user_hp)
        print(user_mp)
        print(user_name)
        print(user_job)
    elif menu_sel == 2:
        print(user_utils[user_job]['스킬'])
    elif menu_sel == 3:
        print(user_utils[user_job]['소지품'])
    elif menu_sel == 4:
        print('창을 종료합니다')
        break
    else:
        print('해당 메뉴를 찾을수 없습니다.')
        
