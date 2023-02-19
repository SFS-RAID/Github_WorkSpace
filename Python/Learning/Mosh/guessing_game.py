import random

print('hello user')
maxguessno = 3
guesscount = 0
secretnum = random.randint(1, 10)
print('Find the secret number!')
print('The number is in between 1 and 10')
while guesscount < maxguessno:
    guess = int(input('Guess: '))
    if guess == secretnum:
        print('You win!')
        break
    guesscount += 1
else:
    print('You lose!')
    print(f'The number was {secretnum}')

