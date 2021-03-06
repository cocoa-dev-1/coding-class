import operator
import random
import time

category_selected = False
category_selected_name = ''
category_answer = []
category_dic = { 
    '역사': [
        ['청동기 시대에 커다란 돌을 쌓아 만든 무덤의 이름은 고인돌 이다. O,X', 'O', '청동기 시대에 커다란 돌을 쌓아 만든 무덤의 이름은 고인돌이 맞다.'],
        ['발해를 세운 왕은 주몽이다. O,X', 'X', '발해를 세운 왕은 대조영이다.'],
        ['일본은 1592년에 임진왜란을 일으켰다. O,X', 'O', '일본은 1592년에 임진왜란을 일으킨게 맞다.'],
        ['이순신 장군이 적군을 한산도 앞바다로 유인하여 학익진 전법으로 이긴 싸움은 명량 대첩이다. O,X', 'X', '한산도 앞바다에서 학익진 전법으로 이긴 싸움은 한산도대첩이다.'],
        ['훈민정음을 만든 사람은 세종대왕이다. O,X', 'O', '훈민정음을 만든 사람은 세종대왕이 맞다.'],
        ['10만 양병설을 주장한 사람은 퇴게 이황이다. O,X', 'X', '10만 양병설을 주장한 사람은 율곡 이이이다.'],
        ['조선 시대에 일본으로 보내던 사신으로 오늘날의 외교 사절에 해당하는 것은 통신사 이다. O,X', 'O', '조선에서 일본으로 보내던 사신은 통신사가 맞다.'],
        ['자유당의 부정과 3.15 부정선거를 계기로 일어난 일은 6월 민주항쟁 이다. O,X', 'X', '3.15 부정선거를 계기로 일어난 일은 4.19 혁명이다.'],
        ['세게에서 가장 오래된 목판 인쇄물은 팔만 대장경이다. O,X', 'X', '세계에서 가장 오래된 목판 인쇄물은 무구정광다라니경 이다.'],
        ['국제 통화 기금(IMF)의 긴급 지원을 요청했던 정부는 김영삼 정부이다. O,X', 'O', '국제 통화 기금(IMF)를 요청한 정부는 김영삼 정부가 맞다.']
    ],
    '수도': [
        ['캄보디아의 수도는 프놈펜 이다. O,X', 'O', '캄보디아의 수도는 프놈펜이 맞다.'],
        ['인도의 수도는 뭄바이 이다. O,X', 'X', '인도의 수도는 뉴 델리 이다.'],
        ['쿠웨이트의 수도는 쿠웨이트 이다. O,X', 'O', '쿠웨이트의 수도는 쿠웨이트 이다.'],
        ['아랍 에미리트 연방의 수도는 두바이 이다. O,X', 'X', '아랍 에미리트 연방의 수도는 아부다비 이다.'],
        ['러시아의 수도는 모스크바 이다. O,X', 'O', '러시아의 수도는 모스크바 이다.'],
        ['노르웨이의 수도는 코펜하겐이다. O,X', 'X', '노르웨이의 수도는 오슬로 이다.'],
        ['캐나다의 수도는 토론도 이다. O,X', 'X', '캐나다의 수도는 오타와 이다.'],
        ['미국의 수도는 워싱턴 D.C 이다. O,X', 'O', '미국의 수도는 워싱턴 D.C 이다.'],
        ['뉴질랜드의 수도는 캔버라 이다. O,X', 'X', '뉴질랜드의 수도는 웰링턴 이다.'],
        ['이집트의 수도는 카이로 이다. O,X', 'O', '이집트의 수도는 카이로 이다.']
    ],
    '상식': [
        ['‘국민의, 국민에 의한, 국민을 위한 정부’라는 말을 한 사람은 링컨이다. O,X', 'O', '‘국민의, 국민에 의한, 국민을 위한 정부’라는 말을 한 사람은 링컨이다.'],
        ['‘너 자신을 알라.’라는 유명한 말을 남긴 철학자는 플라톤 이다. O,X', 'X', '‘너 자신을 알라.’라는 유명한 말을 남긴 철학자는 소크라테스이다.'],
        ['우리나라에서 가장큰 섬은 제주도 이다. O,X', 'O', '우리나라에서 가장큰 섬은 제주도 이다.'],
        ['노인과 바다의 작가는 톨스토이 이다. O,X', 'X', '노인과 바다의 작가는 헤밍웨이 이다.'],
        ['백범 일지를 기록한 사람은 김구 이다. O,X', 'O', '백범일지를 기록한 사람은 김구 이다.'],
        ['생각하는 사람을 조각한 사람은 미켈란젤로 이다. O,X', 'X', '생각하는 사람을 조각한 사람은 로뎅 이다.'],
        ['국가권력의 작용을 입법 · 행정 · 사법의 셋으로 나누어, 국가의 남용을 방지하는 통치조직원리인 이것은 삼권 분립 이다. O,X', 'O', '국가권력의 작용을 입법 · 행정 · 사법의 셋으로 나누어, 국가의 남용을 방지하는 통치조직원리인 이것은 삼권 분립 이다.'],
        ['대한민국애서 면적이 가장 큰 지역은 강원도 이다. O,X', 'X', '대한민국 에서 면적이 가장 큰 지역은 경상북도 이다.'],
        ['노벨상 분야는 총 6개로 - 생리의학상, 물리학상, 화학상, 문학상, 경제학상, 평화상 이 있다. O,X', 'O', '노벨상 분야는 총 6개로 - 생리의학상, 물리학상, 화학상, 문학상, 경제학상, 평화상 이다.'],
        ['2001년~2010년 세계 암센터 기준. (폐암/위암/간암/갑상선암/대장암) 5가지의 암 중에 생존률이 가장 낮은 암은 폐암 이다. O,X', 'X', '2001년~2010년 세계 암센터 기준. (폐암/위암/간암/갑상선암/대장암) 5가지의 암 중에 생존률이 가장 낮은 암은 간암 이다.']
    ]
}
user_input = False
current_user = ''
old_user_info = {}


def get_files(file_name):
    f = open('{0}.txt'.format(file_name), 'r')
    user_dic = {}
    user_list = list(f.read().split('\n'))
    for v in user_list:
        if not v:
            continue
        user_dic[v.split()[0]] = int(v.split()[1])
    f.close()
    return user_dic

def write_files(file_name, text):
    f = open('{0}.txt'.format(file_name), 'a')
    f.write(text)
    f.close()


def category_etc(selected):
    global category_selected
    global old_user_info
    category_selected = True
    if selected == len(category_dic)+1:
        user_rank = sorted(old_user_info.items(), key = operator.itemgetter(1), reverse = True)
        for i, v in enumerate(user_rank):
            print('{0}등 {1}님 점수: {2}'.format(i+1, v[0], v[1]))
        category_selected = False
    else:
        print('게임이 종료되었습니다. ')

def show_answer_f(show_answer):
    global user_input
    global category_selected
    global category_selected_name
    global category_answer
    global old_user_info
    f = open('quiz_rank.txt', 'w')
    for k, v in old_user_info.items():
        f.write('{0} {1}\n'.format(k, v))
        print(k, v)
    f.close()
    if show_answer == 'y':
        for k, v in enumerate(category_answer):
            if v == 'X':
                print('{0}번 정답: {1} 해설: {2}'.format(k+1, category_dic[category_selected_name][k][1],category_dic[category_selected_name][k][2]))
    category_answer = []
    print('게임을 재시작 하시겠습니까? (y,n)')
    inp = input().lower()
    if inp == 'y':
        user_input = False
    elif inp == 'n':
        category_selected = False
    init()
        

def selected_category(selected):
    global category_selected
    global category_selected_name
    correct_aswer = 0
    for k, v in enumerate(category_dic):
        if k == selected:
            print('selected')
            category_selected_name = v
            category_selected = True
            random.shuffle(category_dic[v])
            count = 0
            for question, answer, comment in category_dic[v]:
                count += 1
                print('{0}번 {1}'.format(count, question))
                user_answer = input().upper()
                if user_answer == answer:
                    category_answer.append('O')
                    correct_aswer += 1
                else:
                    category_answer.append('X')
    if correct_aswer > old_user_info[current_user]:
        old_user_info[current_user] = correct_aswer
    print('맞춘 갯수: {0}/10'.format(correct_aswer))
    print('틀린 문제의 해설을 보시겠습니까? (y,n)')
    show_answer = input().lower()
    show_answer_f(show_answer)

if __name__ == '__main__':
    def init():
        global user_input
        global current_user
        global category_selected
        global category_dic
        global old_user_info

        while user_input == False:
            print('유저 정보를 입력해 주세요.')
            user_name = input('유저 아이디: ')
            old_user_info = get_files('quiz_rank')
            print(old_user_info)
            current_user = user_name
            if user_name in old_user_info:
                print('{0}님 안녕하세요. 게임에 접속하신 것을 환영합니다.'.format(user_name))
                user_input = True
                category_selected = False
            else:
                print('신규유저 {0}님 안녕하세요. 게임에 접속하신 것을 환영합니다.'.format(user_name))
                write_files('quiz_rank', '\n{0} 0'.format(user_name))
                old_user_info[user_name] = 0
                user_input = True
                category_selected = False

        while category_selected == False:
            print('카테고리를 선택하세요.')
            for k, v in enumerate(category_dic):
                print('{0}. {1}'.format(k+1, v))
            print('{0}. {1}'.format(len(category_dic)+1, '순위보기'))
            print('{0}. {1}'.format(len(category_dic)+2, '종료하기'))
            category_input = int(input())
            if category_input in [len(category_dic)+1,len(category_dic)+2]:
                category_etc(category_input)
            else:
                selected_category(category_input-1)
    
    init()

    