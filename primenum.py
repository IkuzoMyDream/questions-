# n%1 == 0
# n%n == 0
n = int(input())
start = 2
end = n-1
while True:
    if n == 1:
        print('No')
        break
    if n%start == 0:
        print('No')
        break
    if start == end:
        print('Yes')
        break
    start += 1
