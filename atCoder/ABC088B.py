numN = int(input())
cards = list(map(int, list(input().split())))
cards.sort(reverse=True)

alice = []
bob = []
for cnt in range(numN):
  if (cnt + 1) % 2 == 0:
    bob.append(cards[cnt])
  else:
    alice.append(cards[cnt])

print(sum(alice) - sum(bob))