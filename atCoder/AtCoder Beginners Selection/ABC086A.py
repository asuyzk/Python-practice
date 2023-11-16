inVal = input()
inValArr = inVal.split()

product = int(inValArr[0]) * int(inValArr[1])
remainder = product % 2

if remainder == 1:
  print("Odd")
else:
  print("Even")