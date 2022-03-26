n = int(input())
x = 2
k = 1
y = n
for i in range(n):
    for j in range(1,x+1):
        print((n)*' ' + '*'*k + (n)*' ')
        k += 2
        n -= 1
    k = 1
    x += 1
    n = y
print(' '*n + '|')
print('='*n +'V'+ '='*n)
