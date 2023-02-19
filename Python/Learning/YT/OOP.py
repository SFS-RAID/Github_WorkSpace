import colorama
from colorama import Fore
import os
os.system('cls')

#Create a Class 'Person'
class person:
    is_human = True
    speed = 15
    def __init__(self, name, age, gender = 'male') -> None:
        #Underscore is for Private Variables
        self._name = name
        self._age = age
        self._gender = gender
    
    def talk(self):
        return f"Hello, I am {self._name}"
    
    #This Method is used to change the whole class
    @classmethod
    def changespeed_wholeclass(cls, newspeed):
        #The cls is used to change the Class variable
        cls.speed = newspeed
    
    @property
    def obj_speed(self):
        return self.speed
    
    @obj_speed.setter
    def obj_speed(self, newspeed):
        self.speed = newspeed
    
    #Define a property of age, this can alse be used to show the value of the variable
    @property
    def age(self):
        return self._age
    
    #Set the a value for age property, this is called whenever the age is set
    @age.setter
    def age(self, newage):
        if newage > 125:
            print(f'{newage} is an Invalid Value')
        else:
            self._age = newage
    
    #A Normal Function, It is Used whenever the function being inside the class makes sense
    @staticmethod
    def SayHI(name):
        return 'Hello, i am ' + name

farhan = person('Farhan', 14)
print(Fore.RED + 'Program Running' + colorama.Style.RESET_ALL)
print(farhan.talk())
print('My Speed is' , farhan.obj_speed)

#Change the Speed of the whole Class
person.changespeed_wholeclass(65)

print('The New Class Speed is' , farhan.obj_speed)

#Change the Speed of only the Farhan Object
farhan.obj_speed = 10
print('My New Personal Speed is' , farhan.obj_speed)

print(f'My Age is {farhan.age}')
farhan.age = 127
print(f'I Grew up, My age is {farhan.age}')