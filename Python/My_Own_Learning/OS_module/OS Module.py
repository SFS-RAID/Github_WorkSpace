import os
import shutil

if os.path.exists('TestDir') and os.path.isdir('TestDir'):
    shutil.rmtree('TestDir')

pdir = os.getcwd()
print(pdir)
print('\nThe process has started')
print('\nThe current files in OS Module are', os.listdir())

os.mkdir('TestDir')
print('TestDir has been created')

os.chdir('TestDir')

print('\nSomeFile is created')
with open('SomeFile.txt', 'w') as f:
    f.write('Some data')

print('SomeFile is read')
with open('SomeFile.txt', 'r') as f:
    data = f.read()

with open('AnotherFile.txt', 'w') as f:
    pass
print('Another file has been created')

print(f'The data in SomeFile is "{data}"')
print('\nThe files in TestDir are', os.listdir())

os.remove('AnotherFile.txt')
print('AnotherFile has been removed')
print('\nThe files in TestDir are', os.listdir())

os.chdir('..')
print('\nThe directory has been changed to OS Module')
print(f'The final files in OS Module are {os.listdir()}')
