rankcard = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'J', 'Q', 'K']
sortedrankcard = []

n = input( ).split( )

for i in range(len(n)):
    sortedrankcard.append(rankcard.index(n[i]))

x = sorted(sortedrankcard)
ans = []

for i in range(len(n)):
    ans.append(rankcard[x[i]])

print(" ".join(ans))
