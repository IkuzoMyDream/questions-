n = input( )
ls = []
x = ' '.join(ls)

for i in range(len(n)):
    ls.append(n[i])
x = ' '.join(ls)
print(len(x))

j = 2
k = 0

for i in range(len(n)):
    print(f'{" " * (len(x) - 1 - k)}{x[-(len(x) - k):0:-1]}{x[0]}{x[1: j]}')
    j += 2
    k += 2
