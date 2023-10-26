inVal = input()
inValList = list(inVal)

result = 0
for elem in inValList:
  elem = int(elem)

  if elem == 1:
    result+=1

print(result)