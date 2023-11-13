numN = int(input())
plan = ["0 0 0"] + [input() for cntIn in range(numN)]

flag = 0
for cntN in range(1, numN + 1):
  behindP = list(map(int, plan[cntN-1].split()))
  curtP = list(map(int, plan[cntN].split()))

  if curtP[1] == behindP[1] and curtP[2] == behindP[2]:
    flag = 1
    break
  elif curtP[0] < curtP[1] + curtP[2]:
    flag = 1
    break
  elif curtP[0] - 1 == curtP[1] + curtP[2]:
    flag = 1
    break

if flag == 0:
  print("Yes")
else:
  print("No")