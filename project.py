import random

def coin_toss():
    choice = random.randint(0, 1)
    
    if choice == 0:
        print('Heads')
        return 'Heads'
    
    elif choice == 1:
        print('Tails')
        return 'Tails'

guess = input('Heads or Tails? ')
result = coin_toss()

if guess == result:
    print('Congratulations! Your guess is correct.')
else:
    print('Sorry. Your guess is incorrect.')
