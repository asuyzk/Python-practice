numN = int(input())
numD = []
for _ in range(numN):
  numD.append(int(input()))

print(len(set(numD)))