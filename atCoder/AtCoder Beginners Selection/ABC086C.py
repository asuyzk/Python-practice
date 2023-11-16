numN = int(input())
plan = ["0 0 0"] + [input() for cntIn in range(numN)]

flag = 0
for cntN in range(1, numN + 1):
  behindP = list(map(int, plan[cntN-1].split()))
  curtP = list(map(int, plan[cntN].split()))

  moveTime = curtP[0] - behindP[0]
  if curtP[1] >= behindP[1]:
    moveX = curtP[1] - behindP[1]
  else:
    moveX = behindP[1] - curtP[1]

  if curtP[2] >= behindP[2]:
    moveY = curtP[2] - behindP[2]
  else:
    moveY = behindP[2] - curtP[2]

  # movePrint = [moveTime, moveX, moveY]
  # print(movePrint)
  if curtP[1] == behindP[1] and curtP[2] == behindP[2]:
    flag = 1
    break
  elif curtP[0] < curtP[1] + curtP[2]:
    flag = 1
    break
  elif curtP[0] - 1 == curtP[1] + curtP[2]:
    flag = 1
    break
  elif moveTime < moveX + moveY:
    flag = 1
    break

if flag == 0:
  print("Yes")
else:
  print("No")