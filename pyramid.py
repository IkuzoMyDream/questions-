n = int(input())
def pyramid(n):
 plus = 1
 for i in range(1,n+1):
    print(" "*(n-i) +'*'*plus + ' '*(n-i))
    plus += 2


pyramid(n)
