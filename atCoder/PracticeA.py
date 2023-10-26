total = 0
argStr = ""
while True:
  inVal = input()
  inValArr = inVal.split()

  for cnt in range(0, len(inValArr)): 

    curtVal = inValArr[cnt]
    if curtVal.isdigit() == True: 
      total = total + int(curtVal)
    else:
      argStr = curtVal
  
  if argStr != "":
    break

print(str(total) + " " + argStr)