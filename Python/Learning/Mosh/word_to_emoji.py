i = input('>')
words = i.split(' ')
output = ''
di = {
    'happy' : ':)',
    'sad' : ':('
}
for word in words:
    output += di.get(word, word) + ' '
print(output)