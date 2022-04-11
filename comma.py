n = input()
val = ''

for i in range(1,len(n)+1):
	if len(n) == 3:
		print(n)
		break
	elif len(n[-1:-i-1:-1])%3 == 0:
		val += n[-i]
		val += ','
	else:
		val += n[-i]

vals = val[::-1]

if len(n)%3 == 0:
	print(vals[1:])
else:
	print(val[::-1])
