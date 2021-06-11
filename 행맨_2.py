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
        print('이미 사용된 문자입니다.')
        return curr
    if char in word:
        curr = set_correct_letters(char, word, curr)
    else:
        chance -= 1
    used_alphabet.append(char)

    return curr

def display_used_letters(used):
    for i in used:
        print(i, end=' ')
    print(' ')
    
def display_current_word(curr):
    print(curr)
    print(' ')

def display_hangman(chance):
    if chance <= 5:
        print_head()
    
    if chance == 4:
        print_body()
    elif chance == 3:
        print_left_arm()
    elif chance <= 2:
        print_right_arm()
        if chance == 1:
            print_left_leg()
        elif chance == 0:
            print_right_leg()
    print(' ')



def print_head():
    print('   |   ')
    print('   O   ')

def print_left_arm():
    print('  /|   ')
    print('   |   ')

def print_body():
    print('   |   ')
    print('   |   ')

def print_right_arm():
    print('  /|\\ ')
    print('   |   ')

def print_left_leg():
    print('  /    ')

def print_right_leg():
    print('  / \\ ')


def run_game():
    global chance
    global used_alphabet
    selected = select_word()
    currword = conver_to_underlines(selected)
    used_alphabet = []
    chance = 6
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
            display_hangman(chance)
            display_current_word(currword)
            display_used_letters(used_alphabet)
            if chance == 0:
                print('실패 하였습니다.\n정답: {0}\n맞춘 단어: {1}'.format(selected, currword))
                print('재시작 하시겠습니까?')
                if input() == 'y':
                    run_game()
                    break
                else:
                    break

run_game()