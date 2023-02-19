questions = ['What is your name?', 'How old are you?', 'What is your favourite colour?']
answers = ['Farhan', 14, 'Blue']

for q, a in zip(questions, answers):
    print(f'{q}\nAns:{a}\n')