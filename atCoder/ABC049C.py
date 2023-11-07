inS = input()
strS = list(inS)

strT = []
cnt = 0
while len(strS) >= 5:
  s8 = "".join(strS[cnt:cnt+8])

  if "dreamer" in s8:
    if "dreamera" in s8:
      strT.append("dream")
      cnt += 5
    else:
      strT.append("dreamer")
      cnt += 7
  elif "eraser" in s8:
    strT.append("eraser")
    cnt += 6
  elif "dream" in s8:
    strT.append("dream")
    cnt += 5
  elif "erase" in s8:
    strT.append("erase")
    cnt += 5
  else:
    break
  
  # print("".join(strT))

if inS == "".join(strT):
  print("YES")
else:
  print("NO")
