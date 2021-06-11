import random

wordlist = ['cocoa','banana', 'pineapple']
alphabet = [chr(i) for i in range(97, 123)]
used_alphabet = []
immutable_chance = 6
chance = 6

def select_word():
    return random.choice(wordlist)

def conver_to_underlines(word):
    underbar = ''
    for _ in range(len(word)):
        underbar += '_'
    return underbar

def set_correct_letters(char, word, curr):
    newLetter = ''
    for i in range(len(word)):
        if char == word[i]:
            newLetter += word[i]
            continue
        newLetter += curr[i]
    return newLetter

def is_solved(curr):
    if '_' in curr:
        return False
    return True

def guess(char, word, curr, used):
    global used_alphabet
    global chance
    if char in used:
        return curr
    if char in word:
        curr = set_correct_letters(char, word, curr)
    else:
        chance -= 1
    print(char)
    used_alphabet.append(char)

    return curr

def display_used_letters(used):
    for i in used:
        print(i, end=' ')
    print(' ')
    
def display_current_word(curr):
    print(curr)

def display_hangman(chance):
    hang_list = [print_start, print_head, print_body, print_left_arm, print_right_arm, print_left_leg, print_right_leg]
    hang_list[immutable_chance-chance]()

def print_start():
    print('''
    ____
    |   |
    |   
    |
    |
    |
    ㅡㅡㅡㅡ
    ''') 

def print_head():
    print('''
    ____
    |   |
    |   O
    |
    |
    |
    ㅡㅡㅡㅡ
    ''')

def print_left_arm():
    print('''
    ____
    |   |
    |   O
    |  /|
    |   |
    |
    ㅡㅡㅡㅡ
    ''')

def print_body():
    print('''
    ____
    |   |
    |   O
    |   |
    |   |
    |
    ㅡㅡㅡㅡ
    ''')

def print_right_arm():
    print('''
    ____
    |   |
    |   O
    |  /|\\
    |   |
    |
    ㅡㅡㅡㅡ
    ''')

def print_left_leg():
    print('''
    ____
    |   |
    |   O
    |  /|\\
    |   |
    |  / 
    ㅡㅡㅡㅡ
    ''')

def print_right_leg():
    print('''
    ____
    |   |
    |   O
    |  /|\\
    |   |
    |  / \\
    ㅡㅡㅡㅡ
    ''')


def run_game():
    global chance
    global used_alphabet
    selected = select_word()
    currword = conver_to_underlines(selected)
    used_alphabet = []
    chance = 6
    display_hangman(chance)
    print(currword)
    display_used_letters(used_alphabet)
    while True:
        user_input = input()
        if user_input in alphabet:
            currword = guess(user_input, selected, currword, used_alphabet)
        if is_solved(currword):
            print('축하합니다!')
            print('맞춘 단어: {0}'.format(currword))
            print('재시작 하시겠습니까?')
            if input() == 'y':
                run_game()
                break
            else:
                break
        else:
            if chance != 0:
                display_hangman(chance)
                print(currword)
                display_used_letters(used_alphabet)
            else:
                print('실패 하였습니다.\n맞춘 단어: {0}'.format(currword))
                if input() == 'y':
                    run_game()
                    break
                else:
                    break

run_game()