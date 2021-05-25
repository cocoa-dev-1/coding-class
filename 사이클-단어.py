woord_list = []

for i in range(int(input())):
  result2 = True
  a = input()
  woord_list.append(a) if i == 0 else None
  for j in range(len(a)):
    result = a[j:]+a[:j]
    if result in woord_list:
      result2 = True
      break
    else:
      result2 = False
  
  if result2 == False:
    woord_list.append(a)
    
print(len(woord_list))