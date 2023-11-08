numN = int(input())
timeT = ["0 0 0"]
timeT = timeT + [input() for cntIn in range(numN)]
print(timeT)

flag = 0
for cntN in range(1, numN + 1):
  behindP = list(map(int, timeT[cntN-1].split()))
  curtP = list(map(int, timeT[cntN].split()))
  print(str(curtP) + " - " + str(behindP))

  if curtP[0] < curtP[1] - behindP[1] or curtP[0] < curtP[2] - behindP[2]:
    flag = 1
    break

if flag == 0:
  print("YES")
else:
  print("NO")