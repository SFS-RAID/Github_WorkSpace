print('Hello user!')
car_started = False
car_stopped = False
run = True
command = 'not defined'

while command.lower() != 'quit':
    command = input('>')
    if command.lower() == 'start':
        if car_started == False:
            print('The car has been started......')
            car_started = True
            car_stopped = False
        elif car_started == True:
            print('The car has already been started!')
    elif command.lower() == 'stop':
        if car_stopped == False:
            print('The car has been stopped......')
            car_stopped = True
            car_started = False
        elif car_stopped == True:
            print('The car has already been stopped!')
    elif command.lower() == 'help':
        print('Start - Starts the car')
        print('Stop - Stops the car')
        print('Quit - Quits the game')
    elif command.lower() == 'quit':
        print('Game stopped')
    else:
        print('Invalid Command')