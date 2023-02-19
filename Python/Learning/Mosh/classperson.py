class person:
    def __init__(self, name):
        self.name = name
        
    def talk(self):
        print(f'Hello, i am {self.name}')
        
class boy(person):
    def fe(self):
        print('I am smart')
        
class girl(person):
    def fe(self):
        print('I am cute')
        
farhan = boy('Farhan')
farhan.talk()
farhan.fe()

fariha = girl('Fariha')
fariha.talk()
fariha.fe()
    