import random

people = ['Farhan', 'Fariha', 'Wahab']
ch = random.choice(people)
don = random.random()
if round(don) == 1:
    fe = 'Donkey'
else:
    fe = 'Good'
    
print(f'{ch} is {fe}')

