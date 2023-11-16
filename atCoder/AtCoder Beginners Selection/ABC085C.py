inVal = list(map(int,list(input().split())))
numN = inVal[0]
numY = inVal[1]

bills = [10000, 5000, 1000]
divBills = [0, 0, 0]
for cnt in range(len(bills)):
  divBills[cnt] = numY // bills[cnt]
print(divBills)

cntBills = [0, 0, 0]
factBills = [-1, -1, -1]
for cnt1k in range(divBills[2] + 1):
  for cnt5k in range(divBills[1] + 1):
    for cnt10k in range(divBills[0] + 1):
      cntBills = [cnt10k, cnt5k, cnt1k]

      if sum(cntBills) == numN:
        amount = [bills[i] * cntBills[i] for i in range(3)]
        # print(str(cntBills) + str(sum(amount)))

        if sum(amount) == numY:
          factBills = cntBills
          break
    else:
      continue
    break
  else:
    continue
  break

print(*factBills)