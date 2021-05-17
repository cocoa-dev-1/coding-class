s = input()

phone = s[-4:]
a = ''

for _ in range(len(s)-len(phone)):
    a += '*'

print(a+phone)
