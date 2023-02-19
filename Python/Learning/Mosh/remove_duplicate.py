lis = [4, 9, 2, 0, 9]
print(f'The old list is {lis}')
for item in lis:
    if lis.count(item) > 1:
        lis.reverse()
        lis.remove(item)
        lis.reverse()
print(f'The new list is {lis}')
