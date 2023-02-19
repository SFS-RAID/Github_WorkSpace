print('hello')
mul = int(input('Show the multiples of what number? '))
maxnum = int(input('What is the maximum number: '))
#numset[1] is i
#numset[0] is num   
numset = [1, 1]
while numset[1] < maxnum:
    if numset[1] % mul == 0 :
        print(f'{mul} x {numset[0]} = {numset[1]}')
        numset[0] += 1
    numset[1] += 1

