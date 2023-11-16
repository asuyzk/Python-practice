inVal = []
for cnt in range(4):
  inVal.append(input())

coins = list(map(int, inVal))

pattern = 0
for cntA in range(coins[0] + 1):
  for cntB in range(coins[1] + 1):
    for cntC in range(coins[2] + 1):
      amountA = cntA * 500
      amountB = cntB * 100
      amountC = cntC * 50
      total = amountA + amountB + amountC

      if total == coins[3]:
        pattern += 1

print(pattern)