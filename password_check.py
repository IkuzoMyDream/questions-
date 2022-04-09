import string

NumList = '0123456789'
CharList = '()?,<>.?/\'";:[]{}!@/#-$%^&*_-+='

LetterList = [i for i in string.ascii_letters]
NumList = [i for i in NumList]
CharList = [i for i in CharList]

def CheckPassword(n):
    val = True
    if not (20 > len(n) > 3):
        val = False
    if not (any(letter1.isupper() for letter1 in n)):
        val = False
    if not (any(letter2.islower() for letter2 in n)):
        val = False
    if not (any(num.isdigit() for num in n )):
        val = False
    if not (any(char in CharList for char in n)):
        val = False
    if val:
        return val

def main ():
    password = n
    if CheckPassword(n):
        print('Valid')
    else:
        print('Invalid')
n = input()
main()
