import random

class player():
    playerguess = ''
    wins = 0
    losses = 0
    
class bot():
    botguess = ''  

options = ['Rock', 'Paper', 'Scissors']

maxtimes = int(input('How many times do you want to play?'))
timesplayed = 0

while timesplayed < maxtimes:
    bot.botguess = random.choice(options)
    p_input = int(input('\nRock(1), Paper(2) or Scissors(3)? : ')) - 1
    player.playerguess = options[p_input]
    print(f'Player Guess: {player.playerguess}')
    print(f'Bot Guess: {bot.botguess}')
    if player.playerguess == bot.botguess:
        print('Draw!')
        
    elif player.playerguess == options[0]:
        if bot.botguess == options[1]:
            print('You Lose!')
            player.losses += 1
        elif bot.botguess == options[2]:
            print('You Win!')
            player.wins += 1
            
    elif player.playerguess == options[1]:
        if bot.botguess == options[2]:
            print('You Lose!')
            player.losses += 1
        elif bot.botguess == options[0]:
            print('You Win!')
            player.wins += 1
            
    elif player.playerguess == options[2]:
        if bot.botguess == options[0]:
            print('You Lose!')
            player.losses += 1
        elif bot.botguess == options[1]:
            print('You Win!')
            player.wins += 1
    
    timesplayed += 1
    if timesplayed == maxtimes:
        print(f'\n\nYou won {player.wins} times and lost {player.losses} times.')
        if player.wins > player.losses:
            print('You Won the Game!')
        elif player.wins < player.losses:
            print('You Lost the Game!')
        elif player.wins == player.losses:
            print('The Game was a Draw!')
        print('Game ended!')
        # again =  input('Do you want to play again?(Yes/No) : ')
        # if again.lower == 'yes':
        #     timesplayed = 0
        #     maxtimes = int(input('How many times do you want to play?'))

# print(f'\n\nYou won {player.wins} times and lost {player.losses} times.')
# if player.wins > player.losses:
#     print('You Won the Game!')
# elif player.wins < player.losses:
#     print('You Lost the Game!')
# elif player.wins == player.losses:
#     print('The Game was a Draw!')
# print('Game ended!')