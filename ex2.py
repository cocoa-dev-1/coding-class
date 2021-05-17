s = input()
a_list = []
b = ''

for i in range(len(s)):
    if b == s[i]:
        a_list.append(a_list[i-1]+1)
    else:
        a_list.append(1)
    b = s[i]

print(max(a_list))
