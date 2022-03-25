ls = []
n = int(input())
def customerinfo():

    for i in range(n*3):
        customerinput = input()
        ls.append(customerinput)
customerinfo()

print('--Customers Information--')
k = 0
a = 1

for j in range(n):
    print(ls[ k ] + ' ' + '(age : '  + str(2017 - int(ls[a]))  + ')')
    k += 3
    a += 3
