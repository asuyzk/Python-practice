inVal = list(map(int,list(input().split())))
numN = inVal[0]
numY = inVal[1]

bills = [10000, 5000, 1000]
divBills = [0, 0, 0]
for cnt in range(len(bills)):
  divBills[cnt] = numY // bills[cnt]

factBills = [-1, -1, -1]
for cnt5k in range(divBills[1] + 1):
  for cnt10k in range(divBills[0] + 1):
    cnt1k = numN - (cnt5k + cnt10k)
    if cnt1k >= 0:
      cntBills = [cnt10k, cnt5k, cnt1k]

      amount = [bills[i] * cntBills[i] for i in range(3)]
      if sum(amount) == numY:
        factBills = cntBills
        break
  else:
    continue
  break

print(*factBills)