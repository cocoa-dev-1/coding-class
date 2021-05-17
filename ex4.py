email = input()
bannedLetter = 'CAMBRIDGE'
email_list = []
resultString = ''

for i in range(len(email)):
    print(type(i))
    if bannedLetter.find(email[i]):
        email_list.append(email[i])

for i in email_list:
    resultString += i

print(resultString)