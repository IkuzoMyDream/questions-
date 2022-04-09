def pyramid(n):
    x = 1
    y = 1

    for i in range(n):
        print(f'{" "*(n-i-1)}{"*"*x}')
        x += 2
    for j in range(n-1,0,-1):
        print(f'{" "*(y)}{"*"*(j)}{"*"*(j-1)}')
        y += 1

n = int(input())
pyramid(n)
