# Number guessing game

# Random number
# Hint giver
# Term_counter
# Wins

import random


# Game variable
n = 0
data = 0
count = 0
running = True
n = random.randint(1, 20)
downLimit = (n-(random.randint(1,13)))
upLimit = (n + (random.randint(1,14)))
if downLimit < 1 :
    downLimit = 1
if upLimit > 20:
    upLimit = 20

print(f'\nNumber lies between {downLimit}-{upLimit}')

def hint_giver(hint):
    if hint % 2 == 0:
        print('Number is Even')
        downLimit = (hint-(random.randint(1,13)))
        upLimit = (hint + (random.randint(1,14)))
        if downLimit < 1 or upLimit > 20:
            downLimit = 1
            upLimit = 20
    else:
        print('Number is odd')
        downLimit = (hint-(random.randint(1,13)))
        upLimit = (hint + (random.randint(1,14)))
        if downLimit < 1 or upLimit > 20:
            downLimit = 1
            upLimit = 20


while running:
    hint_giver(n)
    data = int (input('Enter number :-'))
    count += 1
    if data  == n:
        print('You won', count)
        running = False
    else :
        if data > n :
            print('Too much greater number')
        else :
            print('Too much smaller number ')
