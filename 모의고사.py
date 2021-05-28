

first = [1,2,3,4,5]
secound = [2,1,2,3,2,4,2,5]
third = [3,3,1,1,2,2,4,4,5,5]
main_list = []
result_list = []

answer = list(map(int, input().split()))
first_result = 0
first_count = 0
for i in range(len(answer)//len(first)):
    for a in first:
        first_result += 1 if a == answer[first_count] else 0
        first_count += 1
f = len(answer)%len(first)
print(f)
for i in range(f):
  first_result += 1 if first[i] == answer[first_count] else 0
  first_count += 1
main_list.append(first_result)


secound_result = 0
secound_count = 0
for i in range(len(answer)//len(secound)):
    for a in secound:
        secound_result += 1 if a == answer[secound_count] else 0
        secound_count += 1
s = len(answer)%len(secound)
print(s)
for i in range(s):
  secound_result += 1 if secound[i] == answer[secound_count] else 0
  secound_count += 1
main_list.append(secound_result)
    
third_result = 0
third_count = 0
third_rest = len(answer)%len(third)
for i in range(len(answer)//len(third)):
    for a in third:
        third_result += 1 if a == answer[third_count] else 0
        third_count += 1
t = len(answer)%len(third)
print(t)
for i in range(t):
  third_result += 1 if third[i] == answer[third_count] else 0
  third_count += 1
main_list.append(third_result)
main_result = 0
for i in main_list:
    print(i)
    if i == max(main_list):
        print(i)
        result_list.append(main_result+1)
        main_result += 1
print(main_list)
result_list.sort()
print(result_list)