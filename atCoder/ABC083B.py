inVal = input()
nums = list(map(int, inVal.split()))

total = 0
for cnt in range(nums[0] + 1):
  spN = list(map(int,list(str(cnt))))
  sumN = sum(spN)

  if sumN >= nums[1] and sumN <= nums[2]:
    total = total + cnt

print(total)