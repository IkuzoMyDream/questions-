n = input()
lower = 0
upper = 0
for i in range(len(n)):
    if n[i].islower():
        lower += 1
    else:
        upper += 1
print(f'UPPER:{upper}')
print(f'LOWER:{lower}')
