import string
oppponent = [i for i in string.ascii_lowercase]
myteam = [i for i in string.ascii_uppercase]

P,p = 1,1
N,n = 3,3
B,b = 3,3
R,r = 5,5
Q,q = 9,9
K,k = 0,0

myteamscore = 0
oppponentscore = 0

analyze = ''
for i in range(8):
    n = input()
    analyze += n

pawnmyteam = analyze.count('P')
pawnoppo = analyze.count('p')
knightmyteam = analyze.count('N')
knightoppo = analyze.count('n')
bishopmyteam = analyze.count('B')
bishopoppo = analyze.count('b')
rookmyteam = analyze.count('R')
rookoppo = analyze.count('r')
queenmyteam = analyze.count('Q')
queenoppo = analyze.count('q')

myteamscore += pawnmyteam*P
myteamscore += knightmyteam*N
myteamscore += bishopmyteam*B
myteamscore += rookmyteam*R
myteamscore += queenmyteam*Q
oppponentscore += pawnoppo*P
oppponentscore += knightoppo*N
oppponentscore += bishopoppo*B
oppponentscore += rookoppo*R
oppponentscore += queenoppo*Q

if myteamscore == oppponentscore:
    print('equal')
else:
    print(myteamscore - oppponentscore)

