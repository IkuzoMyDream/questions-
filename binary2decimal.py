binary_number = input ( )
decimalval = 0
for i in range ( len ( binary_number ) ):
    decimalval += (int( binary_number[i] ) * (2 ** (len ( binary_number )-i-1) ))

print(decimalval)
