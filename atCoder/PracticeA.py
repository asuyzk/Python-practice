# import sys
# args = sys.argv
# argNum = len(sys.argv)

total = 0
argStr = ""
while True:
  inVal = input()
  inValArr = inVal.split()

  for cnt in range(0, len(inValArr)): 
    # print("cnt: " + str(cnt))

    curtVal = inValArr[cnt]
    if curtVal.isdigit() == True: 
      # print("int")
      total = total + int(curtVal)
    else:
      # print("str")
      argStr = curtVal
  
  if argStr != "":
    break

print(str(total) + " " + argStr)