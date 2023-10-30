inVal = list(map(int,list(input().split())))
numY = inVal[1]

bills = [10000, 5000, 1000]
factBills = [0, 0, 0]

for cnt in range(len(bills)):
  while True:
    if numY >= bills[cnt]:
      print(numY)
      factBills[cnt] += 1
      numY = numY - bills[cnt]
    else:
      break
  
  if inVal[0] != sum(factBills):
    factBills = [-1, -1, -1]
  
print(*factBills)