n = input()
ls = ''
for i in range(len(n)):
    if n[i].isupper():
        ls += n[i].lower()
    else:
        ls += n[i].upper()
print(ls)
