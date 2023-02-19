fnum = int(input('Type a number: '))
op = input('Type an Operator: ')
snum = int(input('Type another number: '))
ans = 0
match op:
    case '+':
        ans = fnum + snum
    case '-':
        ans = fnum - snum
    case '*':
        ans = fnum * snum
    case '/':
        ans = fnum / snum
    case _:
        print('Invalid Input')
        
print(f'{fnum} {op} {snum} = {ans}')