def conv(message, dict):
    '''
    Message is the Input,
    Dict is the Dictonary to Search from
    '''
    words = message.split(' ')
    output = ''
    for word in words:
        output += dict.get(word, word) + ' '
    return output

d1 = {
    'name' : 'farhan',
    'age' : '14'
}
    
    
print('hello')
mes = input('>')
print(conv(mes, d1))