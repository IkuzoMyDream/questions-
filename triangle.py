n = int(input())
b = 0
for i in range(1,n+1):
 if i == n:
     if n > 2:
         x = 0
         _ = '_' * x
         for i in range(n):
             _ = '_' * x
             x += 2
         print('/' + _ + '\\')
     else:
         print('/' + '_' * (n) + '\\')
 else:
     print(' ' * (n - i) + '/' + ' ' * b + '\\' + ' ' * (n - i))
 b += 2
