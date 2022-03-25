ls = []

n = int(input())
for i in range(n):
    num_input = int(input())
    ls.append(num_input)

ls.reverse()
for i in range(len(ls)):
    print(ls[i])
