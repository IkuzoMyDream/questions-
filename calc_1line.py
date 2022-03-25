n = input() # input เป็น str เพราะเช็ค len ได้
sum_all = 0
while len(n) > 1:
    for i in range(len(n)): # input 12345
        sum_all += int(n[i]) #15
    n = str(sum_all) #15
    sum_all = 0

print(n)
