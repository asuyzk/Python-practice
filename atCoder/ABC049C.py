inS = input()
strS = list(inS)

strT = []
while len(strS) >= 5:
  s7 = "".join(strS[0:7])

  if "dreamer" in s7:
    strT.append("dreamer")
    del strS[0:7]
  elif "eraser" in s7:
    strT.append("eraser")
    del strS[0:6]
  elif "dream" in s7:
    strT.append("dream")
    del strS[0:5]
  elif "erase" in s7:
    strT.append("erase")
    del strS[0:5]
  else:
    break
  
  print("".join(strT))

if inS == "".join(strT):
  print("YES")
else:
  print("NO")
