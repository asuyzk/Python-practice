data = list(map(int,list(input().split())))
numA = list(map(int,list(input().split())))

ans = "No"
for cnt in range(data[0]):
  if numA[cnt] == data[1]:
    ans = "Yes"

print(ans)