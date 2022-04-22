n,r = [int(i) for i in input().split()]
j = 1
k = n - 2
for i in range(n):
    if i < r:
        print(f'{"-"*(r-i)}{"*"*(n-(2*r)+(i*2))}{"-"*(r-i)}')
    elif i < (n-r):
        print(f'{"*"*n}')
    else:
        print(f'{"-"*j}{"*"*k}{"-"*j}')
        j += 1
        k -= 2
