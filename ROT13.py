a = 'aiyeou'
b = 'bkxznhdcwgpvjqtsrlmf'
A = a.upper()
B = b.upper()
result = ''
print(len(a))
rot13 = input()

for i in rot13:
  if i.isupper() != True:
    if a.find(i) != -1:
      final = a.find(i) + 3
      final = final % len(a)
      result += a[final]
    elif b.find(i) != -1:
      final = b.find(i) + 10
      final = final % len(b)
      result += b[final]
    else:
      result += ' '
  else:
    if A.find(i) != -1:
      final = A.find(i) + 3
      final = final % len(A)
      result += A[final]
    elif B.find(i) != -1:
      final = B.find(i) + 10
      final = final % len(B)
      result += B[final]
    else:
      result += ' '

print(result)

