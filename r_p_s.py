3 r p s 
import random

def play():
    user = input('(r) for rock, (p) for paper, (s) for scissors: ')
    computer = random.choice(['r','p','q'])
    if user == computer:
        return 'tie'

    if is_win(user,computer): # if win == true
        return 'You won!'

    return 'lose man TT'

def is_win(player, opponent):
    #return tru if user win
    # r > s, s > p, p > r
  if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
      or (player == 'p' and opponent == 'r'):
      return  True

print(play())


import random

def play():
    user = input('(r) for rock, (p) for paper, (s) for scissors: ')
    computer = random.choice(['r','p','s'])
    if user == computer:
        again_not = input('ohoh ur so strong, wanna bea me again\n(ok) for continue, (no) for done: ')
        if again_not == 'ok':
            while user == computer:
                user = input('(r) for rock, (p) for paper, (s) for scissors: ')
                computer = random.choice([ 'r', 'p', 's' ])
        else:
            return 'tie'
    if is_win(user, computer):  # if win == true
        return 'You won!'

    return 'lose man TT'

def is_win(player, opponent):
    # return tru if user win
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
     return True
print(play())




