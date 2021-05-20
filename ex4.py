inInt = int(input())

inInt = inInt*10 if inInt<10 else inInt

inInt_list = [inInt]
count = 0

while True:
    f = inInt_list[-1]//10 + inInt_list[-1]%10     # 몫구하기 연산자(숫자 10자릿수) 나머지 연산자(1의 자릿수)
    inInt_list.append(inInt_list[-1]%10*10 + f%10)
    print(inInt_list)
    count += 1
    if inInt == inInt_list[-1]:
        print(count)
        break
        