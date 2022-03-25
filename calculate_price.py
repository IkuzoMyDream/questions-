ls = []
n = int(input())

def calclate():
    for i in range(n):
        input_price = int(input())
        ls.append(input_price)

calclate()
print(str(sum(ls)) + ' ' +'THB')
