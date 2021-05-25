dic = {}

for _ in range(int(input())):
  dic = {}
  for i in range(65,91):
    dic[chr(i)] = 0

  s = input()
  for i in s:
    if i in dic:
      dic[i] += 1 
  
  for a, b in list(dic.items()):
    if b == 0:
      print(ord(a))
  

    
