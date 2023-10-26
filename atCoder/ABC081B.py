for cnt in range(2):
  inVal = input()
  inValArr = inVal.split()
  inValNum = len(inValArr)
  
  if inValNum > 1:
    arrCnt = 0
    opeCnt = 0
    while True:
      for elemNum in range(0,inValNum):
        elem = int(inValArr[elemNum])
  
        if elem % 2 != 1:
          inValArr[elemNum] = elem / 2
          arrCnt+=1
  
      if arrCnt < len(inValArr):
        break
      elif arrCnt == len(inValArr):
        opeCnt+=1
        arrCnt = 0

print(opeCnt)