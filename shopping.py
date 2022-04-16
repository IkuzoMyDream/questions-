size = [ 'S' , 5 , 'M' , 10 , 'L' , 15 , 'XL' , 20 , 'XXL' , 25 ]
type = [ 'underwear' , 20 , 'pants' , 30 , 'skirt' , 30 , 'shirt' , 40 , 'blouse' , 40 ]
color = [ 'red' , 15 , 'blue' , 15 , 'white' , 10 , 'green' , 15 , 'black' , 15 ]
texture = [ 'cotton' , 20 , 'nylon' , 15 , 'spandex' , 25 , 'wool' , 30 , 'linen' , 25 ]

type_inp = int ( input ( ) )
sizeinp = int ( input ( ) )
colorinp = input ( )
textureinp = int ( input ( ) )
amount = int(input())

ty = 0
if type_inp == 1 :
    print ( f'{type [ type_inp - 1 ]} - {type [ type_inp ]}' )
    ty = type [ type_inp ]
elif type_inp == 2 :
    print ( f'{type [ type_inp ]} - {type [ type_inp + 1 ]}' )
    ty = type [ type_inp +1 ]
elif type_inp == 3 :
    print ( f'{type [ type_inp + 1 ]} - {type [ type_inp + 2 ]}' )
    ty = type [ type_inp + 2]
elif type_inp == 4 :
    print ( f'{type [ type_inp + 2 ]} - {type [ type_inp + 3 ]}' )
    ty = type [ type_inp + 3]
elif type_inp == 5 :
    print ( f'{type [ type_inp + 3 ]} - {type [ type_inp + 4 ]}' )
    ty = type [ type_inp + 4 ]

siz = 0
if sizeinp == 1 :
    print ( f'size {size [ sizeinp - 1 ]} - {size [ sizeinp ]}' )
    siz = size [ sizeinp ]
elif sizeinp == 2 :
    print ( f'size {size [ sizeinp ]} - {size [ sizeinp + 1 ]}' )
    siz = size [ sizeinp+1 ]
elif sizeinp == 3 :
    print ( f'size {size [ sizeinp + 1 ]} - {size [ sizeinp + 2 ]}' )
    siz = size [ sizeinp +2]
elif sizeinp == 4 :
    print ( f'size {size [ sizeinp + 2 ]} - {size [ sizeinp + 3 ]}' )
    siz = size [ sizeinp +3]
elif sizeinp == 5 :
    print ( f'size {size [ sizeinp + 3 ]} - {size [ sizeinp + 4 ]}' )
    siz = size [ sizeinp +4]

col = 0
if colorinp == 'R' :
    print ( f'color {color [ 0 ]} - {color [ 1 ]}' )
    col = color [ 1 ]
elif colorinp == 'B' :
    print ( f'color {color [ 2 ]} - {color [ 3 ]}' )
    col = color [ 3 ]
elif colorinp == 'W' :
    print ( f'color {color [ 4 ]} - {color [ 5 ]}' )
    col = color [ 5 ]
elif colorinp == 'G' :
    print ( f'color {color [ 6 ]} - {color [ 7 ]}' )
    col = color [ 7 ]
elif colorinp == 'BK' :
    print ( f'color {color [ 8 ]} - {color [ 9 ]}' )
    col = color [ 9 ]

tex = 0
if textureinp == 1 :
    print ( f'{texture [ textureinp - 1 ]} - {texture [ textureinp ]}' )
    tex = texture [ textureinp ]
elif textureinp == 2 :
    print ( f'{texture [ textureinp ]} - {texture [ textureinp + 1 ]}' )
    tex = texture [ textureinp +1 ]
elif textureinp == 3 :
    print ( f'{texture [ textureinp + 1 ]} - {texture [ textureinp + 2 ]}' )
    tex = texture [ textureinp +2]
elif textureinp == 4 :
    print ( f'{texture [ textureinp + 2 ]} - {texture [ textureinp + 3 ]}' )
    tex = texture [ textureinp +3]
elif textureinp == 5 :
    print ( f'{texture [ textureinp + 3 ]} - {texture [ textureinp + 4 ]}')
    tex = texture [ textureinp +4]

total = ty + siz + col + tex

print(f'amount - {amount}')
print(f'cost - {total}*{amount} = {total*amount}')
